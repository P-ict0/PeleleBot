import pandas as pd
import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel, Trainer, TrainingArguments
from sklearn.model_selection import train_test_split
from src.LLM_testing.config import Config


def fine_tune_model(data_path):
    # Load preprocessed data
    df = pd.read_csv(data_path)
    df['text'] = df['speaker'] + ": " + df['message']
    train_texts, val_texts = train_test_split(df['text'], test_size=0.1)

    # Load pre-trained model and tokenizer
    model = GPT2LMHeadModel.from_pretrained(Config.PRE_TRAINED_MODEL_NAME)
    tokenizer = GPT2Tokenizer.from_pretrained(Config.PRE_TRAINED_MODEL_NAME)

    # Tokenize the texts
    train_encodings = tokenizer(list(train_texts), truncation=True, padding=True)
    val_encodings = tokenizer(list(val_texts), truncation=True, padding=True)

    class ChatDataset(torch.utils.data.Dataset):
        def __init__(self, encodings):
            self.encodings = encodings

        def __len__(self):
            return len(self.encodings['input_ids'])

        def __getitem__(self, idx):
            item = {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}
            return item

    train_dataset = ChatDataset(train_encodings)
    val_dataset = ChatDataset(val_encodings)

    training_args = TrainingArguments(
        output_dir=Config.MODEL_SAVE_PATH,
        num_train_epochs=Config.EPOCHS,
        per_device_train_batch_size=Config.BATCH_SIZE,
        per_device_eval_batch_size=Config.BATCH_SIZE,
        warmup_steps=500,
        weight_decay=0.01,
        logging_dir='./logs',
        logging_steps=10,
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=val_dataset,
    )

    trainer.train()
    model.save_pretrained(Config.MODEL_SAVE_PATH)
    tokenizer.save_pretrained(Config.MODEL_SAVE_PATH)
    print(f"Model fine-tuned and saved to {Config.MODEL_SAVE_PATH}")


if __name__ == "__main__":
    fine_tune_model(Config.PROCESSED_DATA_PATH)
