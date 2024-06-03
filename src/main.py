from src.utils.logger import Logger
from utils.helpers import read_file, plot_dataframe_simple
from data_processing.data_processing import DataProcessor


class Main:
    def __init__(self) -> None:
        self.logger = Logger(__name__).get_logger()

    def run(self, file_path: str) -> None:
        # Read the raw data from the file
        self.logger.info(f"Reading data from {file_path}")
        raw_data = read_file(file_path)

        # Process the data
        self.logger.info("Processing data")
        processor = DataProcessor(raw_data)
        processed_data = processor.process_data()
        plot_dataframe_simple(
            processed_data,
            "Date",
            "Message_Count",
            "Messages per Day",
            "Date",
            "Message Count",
        )


if __name__ == "__main__":
    main = Main()
    main.run(r"C:\Users\rodri\Documents\Proyectos Progra\PeleleBot\data\raw_data.txt")
