
from transformers import Trainer, AutoTokenizer, AutoModelForMaskedLM, TrainingArguments, DataCollatorForLanguageModeling, TrainerCallback, EarlyStoppingCallback, get_linear_schedule_with_warmup
from torch.optim import AdamW
from torch.utils.data import DataLoader
from process_twarc.util import  load_dict, load_tokenizer, get_all_files, load_dataset, suggest_parameter, save_dict
from process_twarc.preprocess import collate_data
import torch
import wandb
import optuna
from ntpath import basename
import shutil
import os

class OptunaCallback(TrainerCallback):
    def __init__(self, trial, should_prune=True):
        self.trial = trial
        self.should_prune = should_prune

    def on_evaluate(self, args, state, control, metrics=None, **kwargs):
        eval_loss = metrics.get("eval_loss")
        self.trial.report(eval_loss, step=state.global_step)
        if self.should_prune and self.trial.should_prune():
            raise optuna.TrialPruned()
        
class StopCallback(TrainerCallback):
    def on_epoch_end(self, args, state, control, logs=None, **kwargs):
        control.should_training_stop = True
        control.should_save = True

def load_datasets(data_dir: str, output_type: str="Dataset"):
    base = lambda file_path: basename(file_path).split(".")[0]
    split_paths = [path for path in get_all_files(data_dir) if base(path) != "test"]
    tokenized_datasets = {k:v for k,v in zip(
        [base(path) for path in split_paths],
        [load_dataset(path, output_type=output_type) for path in split_paths]
    )}
    return tokenized_datasets["train"], tokenized_datasets["validation"], tokenized_datasets["development"]

def get_sampler(config):
    if config["variable_parameters"]["search_type"] == "random":
        sampler = optuna.samplers.RandomSampler()
    if config["variable_parameters"]["search_type"] == "grid":
        search_field = {k:v for k,v in zip(
            config["variable_parameters"]["search_field"].keys(),
            [value["choices"] for value in config["variable_parameters"]["search_field"].values()]
        )}
        sampler = optuna.samplers.GridSampler(search_field)
    return sampler


def initiate_trial(
    data_dir:str,
    path_to_tokenizer: str,
    path_to_model: str,
    checkpoint_dir: str,
    completed_dir: str,
    path_to_config: str,
    path_to_storage: str,
    print_details: bool=True,
    push_to_hub: bool=False,
):
    def compile_parameters(trial, config):
        fixed_parameters = config["fixed_parameters"]
        search_field = config["variable_parameters"]["search_field"]
        
        suggest = lambda variable: suggest_parameter(trial, search_field, variable)
        variable_parameters = {variable: suggest(variable) for variable in search_field.keys()}

        print("\nVariable Params:")
        for key, value in variable_parameters.items():
            print(f"{key}: {value}")
        
        print("\nFixed Params:")
        for key, value in fixed_parameters.items():
            print(f"{key}: {value}")

        parameters = {**fixed_parameters, **variable_parameters}
        return parameters


    def init_wandb_run(trial, config, parameters):

        wandb_run_id = wandb.util.generate_id()

        kwargs = config["wandb_init"]
        project, group, entity = kwargs["project"], kwargs["group"], kwargs["entity"]

        trial_number = str(trial.number+1).zfill(3)
        name = f"trial-{trial_number}"
        run_name = f"{group}/{name}"

        wandb.init(
            project=project,
            group=group,
            entity=entity,
            name=name,
            id=wandb_run_id,
            resume="allow",
            config=parameters
        )
        return wandb_run_id, run_name

    config = load_dict(path_to_config)
    train_dataset, eval_dataset, test_dataset = load_datasets(data_dir)
    tokenizer = load_tokenizer(path_to_tokenizer, AutoTokenizer, print_details=print_details)
    model = AutoModelForMaskedLM.from_pretrained(path_to_model)

    def objective(trial):

        parameters = compile_parameters(trial, config)

        adam_beta1 = parameters["adam_beta1"]
        adam_beta2 = parameters["adam_beta2"]
        adam_epsilon = parameters["adam_epsilon"]
        attention_dropout_prob = parameters["attention_dropout_prob"]
        attention_probs_dropout_prob = parameters["attention_probs_dropout_prob"]
        eval_strategy = parameters["eval_strategy"]
        hidden_dropout_prob = parameters["hidden_dropout_prob"]
        interval = parameters["interval"]
        learning_rate = parameters["learning_rate"]
        load_best_model_at_end = parameters["load_best_model_at_end"]
        lr_scheduler_type = parameters["lr_scheduler_type"]
        logging_steps = parameters["logging_steps"]
        metric_for_best_model = parameters["metric_for_best_model"]
        num_train_epochs = parameters["num_train_epochs"]
        num_warmup_steps = parameters["num_warmup_steps"]
        patience = parameters["patience"]
        per_device_train_batch_size = parameters["per_device_train_batch_size"]
        per_device_eval_batch_size = parameters["per_device_eval_batch_size"]
        report_to = parameters["report_to"]
        save_strategy = parameters["save_strategy"]
        weight_decay = parameters["weight_decay"]
        


        wandb_run_id, run_name = init_wandb_run(trial, config, parameters)
        trial_checkpoint = os.path.join(checkpoint_dir, run_name)
        trial_complete = os.path.join(completed_dir, run_name)

        device = "cuda" if torch.cuda.is_available() else RuntimeError("No GPU available.")

        model.config.hidden_dropout_prob = hidden_dropout_prob
        model.config.attention_dropout_prob = attention_dropout_prob
        model.config.attention_probs_dropout_prob = attention_probs_dropout_prob
        model.to(device)
        
        if print_details:
            print(model.config)

        data_collator = collate_data(DataCollatorForLanguageModeling, tokenizer, train_dataset, per_device_train_batch_size)

        optimizer = AdamW(
            params=model.parameters(),
            lr=learning_rate,
            betas = (adam_beta1, adam_beta2),
            eps=adam_epsilon,
            weight_decay=weight_decay)
        
        scheduler = get_linear_schedule_with_warmup(
            optimizer=optimizer,
            num_warmup_steps=num_warmup_steps,
            num_training_steps=len(train_dataset)//per_device_train_batch_size * num_train_epochs,
            last_epoch = -1
        )

        training_args = TrainingArguments(
            lr_scheduler_type=lr_scheduler_type,
            logging_steps=logging_steps,
            warmup_steps= num_warmup_steps,
            learning_rate=learning_rate,
            adam_beta1=adam_beta1,
            adam_beta2=adam_beta2,
            adam_epsilon=adam_epsilon,
            weight_decay=weight_decay,
            output_dir=trial_checkpoint,
            evaluation_strategy=eval_strategy,
            eval_steps= 1 / interval / num_train_epochs,
            num_train_epochs=num_train_epochs,
            save_strategy=save_strategy,
            save_steps=1 / interval /num_train_epochs,
            save_total_limit=patience,
            push_to_hub=push_to_hub,
            per_device_train_batch_size=per_device_train_batch_size,
            per_device_eval_batch_size=per_device_eval_batch_size,
            load_best_model_at_end=load_best_model_at_end, 
            metric_for_best_model=metric_for_best_model,
            report_to=report_to
        )
        
        custom_args = {
            "patience": patience,
            "wandb_run_id": wandb_run_id,
            "last_train_epoch": 0,
            "attention_dropout_prob": attention_dropout_prob,
            "hidden_dropout_prob": hidden_dropout_prob,
            "attention_probs_dropout_prob": attention_probs_dropout_prob,
        }

        trainer = Trainer(
            model=model,
            args=training_args,
            data_collator=data_collator,
            train_dataset=train_dataset,
            eval_dataset=eval_dataset,
            tokenizer=tokenizer,
            optimizers=(optimizer, scheduler),
            callbacks=[EarlyStoppingCallback(early_stopping_patience=patience),
                       StopCallback()]
        )

        print(f"\nStarting {run_name}. . .")
        trainer.train()
        
        custom_args["last_train_epoch"] = trainer.state.epoch
        # checks to see if the EarlStoppingCallback was triggered by checking if trainer.state.epoch is divisible by 1
        if trainer.state.epoch%1 != 0:
            print("EarlyStoppingCallback triggered.")
            results = trainer.evaluate(test_dataset)
            print("\nResults:", results)
            wandb.log(results)
            trainer.save_model(trial_complete)
            save_dict(custom_args, f"{trial_complete}/custom_args.json")
            #deletes the trial directory
            shutil.rmtree(trial_checkpoint)
        
        else:
            print(f"Training paused. Last train epoch: {custom_args['last_train_epoch']}.")
            save_dict(custom_args, f"{trial_checkpoint}/custom_args.json")
        
        return 1
    
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
    path_to_tokenizer: str,
    path_to_model: str,
    path_to_config: str,
    trial_dir: str,
    completed_dir: str,
    device = "cuda" if torch.cuda.is_available() else RuntimeError("No GPU available."),
    print_details: bool=True,
):
    
    def get_last_checkpoint(trial_dir: str):
        checkpoints = [os.path.join(trial_dir, checkpoint) for checkpoint in os.listdir(trial_dir) if os.path.isdir(os.path.join(trial_dir, checkpoint))]
        return max(checkpoints, key=os.path.getctime)
    
    def compile_parameters(config, last_checkpoint):
        training_args = torch.load(f"{last_checkpoint}/training_args.bin")
        custom_args = load_dict(f"{trial_dir}/custom_args.json")
        training_args_dict = {k:v for k,v in training_args.__dict__.items() if k != "callbacks"}
        parameters = {**training_args_dict, **custom_args}

        print("\nVariable Params:")
        for key in config["variable_parameters"]["search_field"].keys():
            print(f"{key}: {parameters[key]}")

        print("\nFixed Params:")
        for key in config["fixed_parameters"].keys():
            if key in parameters.keys():
                print(f"{key}: {parameters[key]}")



        return training_args, custom_args, parameters
    
    config = load_dict(path_to_config)
    last_checkpoint = get_last_checkpoint(trial_dir)
    run_name = os.path.join(basename(os.path.dirname(trial_dir)), basename(trial_dir))
    trial_complete = os.path.join(completed_dir, run_name)

    training_args, custom_args, parameters = compile_parameters(config, last_checkpoint)

    adam_beta1 = parameters["adam_beta1"]
    adam_beta2 = parameters["adam_beta2"]
    adam_epsilon = parameters["adam_epsilon"]
    attention_dropout_prob = parameters["attention_dropout_prob"]
    attention_probs_dropout_prob = parameters["attention_probs_dropout_prob"]
    hidden_dropout_prob = parameters["hidden_dropout_prob"]
    last_train_epoch = parameters["last_train_epoch"]
    learning_rate = parameters["learning_rate"]
    num_train_epochs = parameters["num_train_epochs"]
    num_warmup_steps = parameters["warmup_steps"]
    patience = parameters["patience"]
    per_device_train_batch_size = parameters["per_device_train_batch_size"]
    wandb_run_id = parameters["wandb_run_id"]
    weight_decay = parameters["weight_decay"]

    train_dataset, eval_dataset, test_dataset = load_datasets(data_dir)
    tokenizer = load_tokenizer(path_to_tokenizer, AutoTokenizer, print_details=print_details)
    model = AutoModelForMaskedLM.from_pretrained(path_to_model)
    model.config.hidden_dropout_prob = hidden_dropout_prob
    model.config.attention_dropout_prob = attention_dropout_prob
    model.config.attention_probs_dropout_prob = attention_probs_dropout_prob
    model.to(device)

    if print_details:
        print(model.config)

    if last_train_epoch + 1 == num_train_epochs:
        final_epoch = True
    else:
        final_epoch = False

    wandb.init(
        project=config["wandb_init"]["project"],
        id=wandb_run_id,
        resume="must")
    
    data_collator = collate_data(DataCollatorForLanguageModeling, tokenizer, train_dataset, per_device_train_batch_size)

    optimizer = AdamW(
        params=model.parameters(),
        lr=learning_rate,
        betas = (adam_beta1, adam_beta2),
        eps=adam_epsilon,
        weight_decay=weight_decay)
    optimizer.load_state_dict(torch.load(f"{last_checkpoint}/optimizer.pt"))

    scheduler = get_linear_schedule_with_warmup(
        optimizer=optimizer,
        num_warmup_steps=num_warmup_steps,
        num_training_steps=len(train_dataset)//per_device_train_batch_size * num_train_epochs,
        last_epoch = last_train_epoch
    )
    scheduler.load_state_dict(torch.load(f"{last_checkpoint}/scheduler.pt"))

    if final_epoch:
        callbacks = [EarlyStoppingCallback(early_stopping_patience=patience)]
    else:
        callbacks = [EarlyStoppingCallback(early_stopping_patience=patience),
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
        results = trainer.evaluate(test_dataset)
        print("\nResults:", results)
        wandb.log(results)
        trainer.save_model(trial_complete)
        save_dict(custom_args, f"{trial_complete}/custom_args.json")
        #deletes the trial directory
        shutil.rmtree(trial_dir)

    elif trainer.state.epoch == num_train_epochs:
        print("Training complete.")
        results = trainer.evaluate(test_dataset)
        print("\nResults:", results)
        wandb.log(results)
        trainer.save_model(trial_complete)
        save_dict(custom_args, f"{trial_complete}/custom_args.json")
        #deletes the trial directory
        shutil.rmtree(trial_dir)

    else:
        print(f"Training paused. Last train epoch: {custom_args['last_train_epoch']}.")
        save_dict(custom_args, f"{trial_dir}/custom_args.json")

    return
