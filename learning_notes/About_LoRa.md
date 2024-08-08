# Low Rank Approximation (LoRA)

- [Low Rank Approximation (LoRA)](#low-rank-approximation-lora)
  - [Introduction](#introduction)
  - [Theoritical LoRA](#theoritical-lora)
  - [Hyperparameter tuning LoRA Parameters](#hyperparameter-tuning-lora-parameters)
  - [HuggingFace Implementation Example](#huggingface-implementation-example)

## Introduction
LoRA (Low Rank Approximation) is a Parameter-Efficient FineTuning (PEFT) method, to achieve minimal computational resource req. with the same effectiveness as full finetuning (in most cases).

Three PEFT method categories:
1. Selective: choose subset of the pre-trained model weight to be fine-tuned.
2. Reparametrization: use low-dimensional representation of a specific module (such as query vector of a transformer model) in the original LLM.
3. Additive: adding new modules into the model for fine-tuning, trained to incorporate new knowledge into the pre-trained LLM.

LoRA is a reparametrization PEFT method, based on observation of the weights learned by LLM after training, often contain redundancies. Instead of fine-tuning the whole weights in the LLM model, focusing on a low rank approx. of the weights (leads to smaller set of weights only) that eliminates the redundancies. During the process, other weights are frozen, to make sure it doesn't alter the process, makes the process more efficient and reduces the risk of overfitting and forgeting.

## Theoritical LoRA
LoRA can be defined using eequation:

$$ W = W_o+\Delta{W}=W_o BA$$

Where:

$W_o$ is pre-trained parameter weights.

$\Delta{W}$ is learned weights to be used in adjusting the original weight.

$W$ is the final fine-tuned weight that will be used during inference.

$B$ is the matrix of dimension $d\times r$ and $A$ is matrix of dimention $r\times K$.

The approach is to fine-tune the matrix decomposition of $\Delta W$ (which is $A$ and $B$) with rank $r$ less than $min(d,k)$ from the original matrix. Leads to smaller trained parameters, means faster and lighter finetuning process.

## Hyperparameter tuning LoRA Parameters
Hyperparameter tuning in LoRA Parameters can be done for:
- `r` leads to smaller number of parameters to finetune, start from small `r` and gradually increase until there is diminishing performance.
- `target modules/layers` selected based on the model architecture & task, use hyperparameter tuning to find the best performance.
- `alpha` is a scaling factor, controls how much new weights from low-rank modules to replace the pre-trained weights. Scaling factor is 1 when `alpha` = `rank`, use this when there is nothing entirely new on the dataset, and the model has enough understanding of language.

## HuggingFace Implementation Example
Using HuggingFace, the steps is:
1. Load the model and dataset
   ```python
    from datasets import load_dataset
    from peft import PeftModel, PeftConfig, LoraConfig, TaskType, get_peft_model
    from transformers import TrainingArguments, Trainer, AutoModelForSequenceClassification, AutoTokenizer

    id2label = {0: "NEGATIVE", 1: "POSITIVE"}
    label2id = {"NEGATIVE": 0, "POSITIVE": 1}


    model= AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased", id2label=id2label, label2id=label2id)
    dataset = load_dataset("rotten_tomatoes")
    dataset
   ```
2. Load the tokenizer
   ```python
    checkpoint = "distilbert-base-uncased"
    tokenizer = AutoTokenizer.from_pretrained(checkpoint)
    def tokenizer_func(input):
        return tokenizer(input["text"],  truncation=True)

    data_collator = DataCollatorWithPadding(tokenizer=tokenizer)
    data_tokenized = data.map(tokenizer_func, batched=True)

    train_data_tokenized = data_tokenized["train"].remove_columns(["text"]).rename_column("label", "labels")
    val_data_tokenized = data_tokenized["validation"].remove_columns(["text"]).rename_column("label", "labels")
   ```
3. Load the LoRA Config
   ```python
    lora_config = LoraConfig(
    r=8, # rank - see hyperparameter section for more details
    lora_alpha=32, # scaling factor - see hyperparameter section for more details
    target_modules=["q_lin", "v_lin"],
    lora_dropout=0.05,
    bias="none",
    task_type=TaskType.SEQ_CLS
    )

    peft_model = get_peft_model(model, lora_config)
    peft_model.print_trainable_parameters()
   ```
4. Train
   ```python
    output_dir = f'./rotten-tomatoes-classification-training-{str(int(time.time()))}'

    training_args = TrainingArguments(
        output_dir=output_dir,
        learning_rate=1e-5,
        logging_steps=1,
        max_steps=10
    )

    trainer = Trainer(
        model=peft_model,
        args=training_args,
        train_dataset=train_data_tokenized,
        eval_dataset=val_data_tokenized,
        data_collator=data_collator,
        tokenizer=tokenizer,
    )

    trainer.train()
   ```
