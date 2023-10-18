
from transformers import Trainer, AutoTokenizer, AutoModelForMaskedLM, TrainingArguments, DataCollatorForLanguageModeling, TrainerCallback, EarlyStoppingCallback, get_linear_schedule_with_warmup
from process_twarc.util import  load_dict, load_tokenizer, save_dict
from process_twarc.preprocess import collate_data
from process_twarc.train.util import load_datasets, init_wandb_run, reinit_wandb_run, get_sampler, configure_dropout, OptunaCallback, StopCallback, get_optimizer, get_scheduler, configure_training_args, get_save_paths
import torch
import wandb
import optuna
from ntpath import basename
import shutil
import os

def initiate_trial(
    data_dir:str,
    checkpoint_dir: str,
    completed_dir: str,
    path_to_config: str,
    path_to_storage: str,
    complete_trial: bool=False,
    should_prune: bool=False,
    print_details: bool=True,
):
    
    config = load_dict(path_to_config)
    train_dataset, eval_dataset, test_dataset = load_datasets(data_dir)

    def objective(trial):

        parameters, wandb_run_id, run_name = init_wandb_run(trial, config)
        trial_checkpoint, trial_complete = get_save_paths(checkpoint_dir, completed_dir, run_name)

        device = "cuda" if torch.cuda.is_available() else RuntimeError("No GPU available.")

        tokenizer = load_tokenizer(parameters["path_to_tokenizer"], print_details=print_details)
        model = AutoModelForMaskedLM.from_pretrained(parameters["path_to_model"])
        model = configure_dropout(model, parameters)
        model.to(device)
        
        if print_details:
            print(model.config)

        data_collator = collate_data(
            DataCollatorForLanguageModeling, 
            tokenizer,
            train_dataset, 
            parameters["per_device_train_batch_size"])
        
        optimizer = get_optimizer(model, parameters)
        scheduler = get_scheduler(train_dataset, parameters, optimizer)

        if complete_trial:
            callbacks = [
                EarlyStoppingCallback(early_stopping_patience=parameters["patience"]),
                OptunaCallback(trial, should_prune=should_prune)
            ]
        else:
            callbacks = [
                EarlyStoppingCallback(early_stopping_patience=parameters["patience"]),
                StopCallback()
            ]

        training_args = configure_training_args(parameters, trial_checkpoint)
        custom_args = {
            "attention_dropout_prob": parameters["attention_dropout_prob"],
            "attention_probs_dropout_prob": parameters["attention_probs_dropout_prob"],
            "hidden_dropout_prob": parameters["hidden_dropout_prob"],
            "last_train_epoch": 0,
            "patience": parameters["patience"],
            "wandb_run_id": wandb_run_id,
        }

        os.makedirs(trial_checkpoint, exist_ok=True)
        save_dict(custom_args, f"{trial_checkpoint}/custom_args.json")

        trainer = Trainer(
            model=model,
            args=training_args,
            data_collator=data_collator,
            train_dataset=train_dataset,
            eval_dataset=eval_dataset,
            tokenizer=tokenizer,
            optimizers=(optimizer, scheduler),
            callbacks=callbacks
        )

        print(f"\nStarting {run_name}. . .")
        trainer.train()
        
        custom_args["last_train_epoch"] = trainer.state.epoch
        # checks to see if the EarlStoppingCallback was triggered by checking if trainer.state.epoch is divisible by 1
        if trainer.state.epoch%1 != 0:
            print("EarlyStoppingCallback triggered.")
            complete = True
        elif trainer.state.epoch == parameters["num_train_epochs"]:
            print("Training complete.")
            complete = True
        else:
            complete = False
            print(f"Training paused. Last train epoch: {custom_args['last_train_epoch']}.")
            save_dict(custom_args, f"{trial_checkpoint}/custom_args.json")
            trial_value = 1
        
        if complete:
            results = trainer.evaluate(test_dataset)
            print("\nResults:", results)
            wandb.log(results)
            trainer.save_model(trial_complete)
            save_dict(custom_args, f"{trial_complete}/custom_args.json")
            #deletes the trial directory
            shutil.rmtree(trial_checkpoint)
            trial_value = results["eval_loss"]
        
        return trial_value
    
    study_name = config["wandb_init"]["group"]
    study = optuna.create_study(
        storage=path_to_storage,
        sampler=get_sampler(config),
        study_name=study_name,
        direction="minimize",
        load_if_exists=True,
        )
    study.optimize(objective, n_trials=1)


def resume_trial(
    data_dir:str,
    path_to_config: str,
    trial_dir: str,
    completed_dir: str,
    complete_trial: bool=False,
    print_details: bool=True,
):
    
    def get_last_checkpoint(trial_dir: str):
        checkpoints = [os.path.join(trial_dir, checkpoint) for checkpoint in os.listdir(trial_dir) if os.path.isdir(os.path.join(trial_dir, checkpoint))]
        return max(checkpoints, key=os.path.getctime)
    
    config = load_dict(path_to_config)
    last_checkpoint = get_last_checkpoint(trial_dir)
    run_name = os.path.join(basename(os.path.dirname(trial_dir)), basename(trial_dir))
    trial_complete = os.path.join(completed_dir, run_name)

    training_args, custom_args, parameters = reinit_wandb_run(last_checkpoint, config)

    train_dataset, eval_dataset, test_dataset = load_datasets(data_dir)
    tokenizer = load_tokenizer(parameters["path_to_tokenizer" ], print_details=print_details)
    device = "cuda" if torch.cuda.is_available() else RuntimeError("No GPU available.")

    model = AutoModelForMaskedLM.from_pretrained(config["fixed_parameters"]["path_to_model"])
    model = configure_dropout(model, parameters)
    model.to(device)

    if print_details:
        print(model.config)
 
    data_collator = collate_data(
        DataCollatorForLanguageModeling, 
        tokenizer, 
        train_dataset, 
        parameters["per_device_train_batch_size"]
        )

    optimizer = get_optimizer(model, parameters)
    optimizer.load_state_dict(torch.load(f"{last_checkpoint}/optimizer.pt"))

    scheduler = get_scheduler(train_dataset, parameters, optimizer)
    scheduler.load_state_dict(torch.load(f"{last_checkpoint}/scheduler.pt"))

    if parameters["last_train_epoch"] + 1 == parameters["num_train_epochs"]:
        final_epoch = True
    else:
        final_epoch = False

    if final_epoch or complete_trial:
        callbacks = [EarlyStoppingCallback(early_stopping_patience=parameters["patience"])]
    else:
        callbacks = [EarlyStoppingCallback(early_stopping_patience=parameters["patience"]),
                        StopCallback()]

    trainer = Trainer(
        model=model,
        args=training_args,
        data_collator=data_collator,
        train_dataset=train_dataset,
        eval_dataset=eval_dataset,
        tokenizer=tokenizer,
        optimizers=(optimizer, scheduler),
        callbacks=callbacks
    )

    print(f"\nResuming {run_name}. . .")
    trainer.train(resume_from_checkpoint=last_checkpoint)

    custom_args["last_train_epoch"] = trainer.state.epoch
    # checks to see if the EarlStoppingCallback was triggered
    if trainer.state.epoch%1 != 0:
        print("EarlyStoppingCallback triggered.")
        complete = True
    elif trainer.state.epoch == parameters["num_train_epochs"]:
        print("Training complete.")
        complete = True
    else:
        complete = False
        print(f"Training paused. Last train epoch: {custom_args['last_train_epoch']}.")
        save_dict(custom_args, f"{trial_dir}/custom_args.json")
    
    if complete:
        results = trainer.evaluate(test_dataset)
        print("\nResults:", results)
        wandb.log(results)
        trainer.save_model(trial_complete)
        save_dict(custom_args, f"{trial_complete}/custom_args.json")
        #deletes the trial directory
        shutil.rmtree(trial_dir)