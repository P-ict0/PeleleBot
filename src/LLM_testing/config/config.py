class Config:
    CHAT_DATA_PATH = 'data/group_chat.txt'
    PROCESSED_DATA_PATH = 'data/preprocessed_data.csv'
    MODEL_SAVE_PATH = 'models/fine_tuned_model/'
    PRE_TRAINED_MODEL_NAME = 'gpt-2'  # You can choose other models like 'distilbert-base-uncased'
    EPOCHS = 3
    BATCH_SIZE = 4
    LEARNING_RATE = 5e-5

