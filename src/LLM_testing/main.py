from utils.preprocessing import preprocess_chat_data
from utils.training import fine_tune_model
from config.config import Config


def main():
    # Step 1: Preprocess the data
    preprocess_chat_data(Config.CHAT_DATA_PATH, Config.PROCESSED_DATA_PATH)

    # Step 2: Fine-tune the model
    fine_tune_model(Config.PROCESSED_DATA_PATH)


if __name__ == "__main__":
    main()
