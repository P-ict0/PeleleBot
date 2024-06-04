import pandas as pd
import re
from src.LLM_testing.config import Config


def preprocess_text(text):
    # Example preprocessing steps: remove special characters, tokenize, etc.
    text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces with a single space
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    return text


def preprocess_chat_data(chat_data_path, output_path):
    with open(chat_data_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    data = {'speaker': [], 'message': []}
    for line in lines:
        if line.strip():  # Ignore empty lines
            parts = line.split(':', 1)
            if len(parts) == 2:
                speaker, message = parts
                data['speaker'].append(speaker.strip())
                data['message'].append(preprocess_text(message.strip()))

    df = pd.DataFrame(data)
    df.to_csv(output_path, index=False)
    print(f"Preprocessed data saved to {output_path}")


if __name__ == "__main__":
    preprocess_chat_data(Config.CHAT_DATA_PATH, Config.PROCESSED_DATA_PATH)
