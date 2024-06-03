import logging
from colorlog import ColoredFormatter


class Logger:
    """A simple console logger class that outputs colorized logs."""

    def __init__(self, name: str) -> None:
        """
        Initialize a colorized console logger.

        Parameters:
        name (str): Name of the logger which is typically the name of the module creating the logger.
        """
        # Create a logger
        self.logger = logging.getLogger(name)
        self.logger.setLevel(
            logging.DEBUG
        )  # Set the threshold of logger to debug level

        # Create console handler and set level to debug
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # Create colored formatter
        formatter = ColoredFormatter(
            "%(log_color)s[%(levelname)s]%(reset)s %(white)s%(message)s",
            datefmt=None,
            reset=True,
            log_colors={
                "DEBUG": "cyan",
                "INFO": "green",
                "WARNING": "yellow",
                "ERROR": "red",
                "CRITICAL": "red,bg_white",
            },
            secondary_log_colors={},
            style="%",
        )

        # Add formatter to console handler
        ch.setFormatter(formatter)

        # Add ch to logger
        self.logger.addHandler(ch)

    def get_logger(self) -> logging.Logger:
        """
        Returns the configured logger with colorized output.
        """
        return self.logger
