from transformers import TrainerCallback, get_constant_schedule_with_warmup, get_linear_schedule_with_warmup, TrainingArguments
from process_twarc.util import  get_all_files, load_dataset, suggest_parameter, load_dict
import torch
from torch.optim import AdamW
import wandb
import optuna
from ntpath import basename
import evaluate
import numpy as np
import os


class OptunaCallback(TrainerCallback):
    def __init__(self, trial, should_prune):
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

def compute_accuracy(eval_pred):
    accuracy = evaluate.load("accuracy")
    predictions, labels = eval_pred
    predictions = np.argmax(predictions, axis=1)
    return accuracy.compute(predictions=predictions, references=labels)


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


def init_wandb_run(trial, config):
    fixed_parameters = config["fixed_parameters"]
    search_field = config["variable_parameters"]["search_field"]
    
    suggest = lambda variable: suggest_parameter(trial, search_field, variable)
    variable_parameters = {variable: suggest(variable) for variable in search_field.keys()}

    parameters = {**fixed_parameters, **variable_parameters}

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

    print("\nVariable Params:")
    for key, value in variable_parameters.items():
        print(f"{key}: {value}")
    
    print("\nFixed Params:")
    for key, value in fixed_parameters.items():
        print(f"{key}: {value}")
    return parameters, wandb_run_id, run_name

def reinit_wandb_run(last_checkpoint, config):
    trial_dir = os.path.dirname(last_checkpoint)
    training_args = torch.load(f"{last_checkpoint}/training_args.bin")
    custom_args = load_dict(f"{trial_dir}/custom_args.json")
    training_args_dict = {k:v for k,v in training_args.__dict__.items() if k != "callbacks"}
    parameters = {**training_args_dict, **custom_args, **config["fixed_parameters"]}

    wandb.init(
        project=config["wandb_init"]["project"],
        id=parameters["wandb_run_id"],
        resume="must"
        )

    print("\nVariable Params:")
    for key in config["variable_parameters"]["search_field"].keys():
        print(f"{key}: {parameters[key]}") 

    print("\nFixed Params:")
    for key in config["fixed_parameters"].keys():
        if key in parameters.keys():
            print(f"{key}: {parameters[key]}")

    return training_args, custom_args, parameters

def get_save_paths(checkpoint_dir, completed_dir, run_name):
    checkpoint_path = os.path.join(checkpoint_dir, run_name)
    completed_path = os.path.join(completed_dir, run_name)
    return checkpoint_path, completed_path



def get_optimizer(model, parameters):
    optimizer = AdamW(
        params=model.parameters(),
        lr=parameters["learning_rate"],
        betas = (parameters["adam_beta1"], parameters["adam_beta2"]),
        eps=parameters["adam_epsilon"],
        weight_decay=parameters["weight_decay"])
    return optimizer

def get_scheduler(train_dataset, parameters, optimizer):
    lr_scheduler_type = parameters["lr_scheduler_type"]
    num_train_epochs = parameters["num_train_epochs"]
    batch_size = parameters["per_device_train_batch_size"]

    if lr_scheduler_type == "constant":
        scheduler = get_constant_schedule_with_warmup(
            optimizer=optimizer,
            num_warmup_steps=parameters["num_warmup_steps"] if "num_warmup_steps" in parameters.keys() else 0
        )
    if lr_scheduler_type == "linear":
        scheduler = get_linear_schedule_with_warmup(
            optimizer=optimizer,
            num_warmup_steps=parameters["num_warmup_steps"],
            num_training_steps= len(train_dataset) // batch_size * num_train_epochs
        )
    return scheduler


def configure_dropout(model, parameters):
    if "hidden_dropout_prob" in parameters.keys():
        model.config.hidden_dropout_prob = parameters["hidden_dropout_prob"]
    if "attention_dropout_prob" in parameters.keys():
        model.config.attention_dropout_prob = parameters["attention_dropout_prob"]
    if "attention_probs_dropout_prob" in parameters.keys():
        model.config.attention_probs_dropout_prob = parameters["attention_probs_dropout_prob"]
    return model

def configure_training_args(
        parameters,
        output_dir
):
    if "interval" in parameters.keys():
        evaluation_strategy = save_strategy = "steps"
        eval_steps = save_steps = 1 / parameters["interval"] / parameters["num_train_epochs"]
    else:
        evaluation_strategy = save_strategy = "epoch"
        eval_steps = save_steps = 1

    training_args = TrainingArguments(
        adam_beta1=parameters["adam_beta1"],
        adam_beta2=parameters["adam_beta2"],
        adam_epsilon=parameters["adam_epsilon"],
        eval_steps=eval_steps,
        evaluation_strategy=evaluation_strategy,
        logging_steps=parameters["logging_steps"],
        learning_rate=parameters["learning_rate"],
        load_best_model_at_end=parameters["load_best_model_at_end"],
        lr_scheduler_type=parameters["lr_scheduler_type"],
        metric_for_best_model=parameters["metric_for_best_model"],
        num_train_epochs=parameters["num_train_epochs"],
        output_dir=output_dir,
        per_device_train_batch_size=parameters["per_device_train_batch_size"],
        per_device_eval_batch_size=parameters["per_device_eval_batch_size"],
        push_to_hub=parameters["push_to_hub"],
        report_to=parameters["report_to"],
        save_strategy=save_strategy,
        save_steps=save_steps,
        save_total_limit=parameters["patience"],
        warmup_steps=parameters["num_warmup_steps"],
        weight_decay=parameters["weight_decay"])

    return training_args