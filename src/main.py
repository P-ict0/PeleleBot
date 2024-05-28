from src.utils.logger import Logger


class Main:
    def __init__(self) -> None:
        self.logger = Logger(__name__).get_logger()

    def test_logger(self) -> None:
        self.logger.debug("This is a debug message.")
        self.logger.info("This is an info message.")
        self.logger.warning("This is a warning message.")
        self.logger.error("This is an error message.")
        self.logger.critical("This is a critical message.")


if __name__ == "__main__":
    main = Main()
    main.test_logger()
