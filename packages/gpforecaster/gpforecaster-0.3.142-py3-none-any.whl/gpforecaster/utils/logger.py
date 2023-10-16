import logging
import os
import time
from gpforecaster import __version__


class ConsoleOnlyFilter(logging.Filter):
    """
    A filter to check if a log record has the attribute `console_only`
    """

    def filter(self, record):
        return not getattr(record, "console_only", False)


class Logger:
    def __init__(
        self, name, dataset, to_file=None, log_level=logging.INFO, log_dir="."
    ):
        self.name = name
        self.dataset = dataset
        self.to_file = to_file
        self.log_dir = log_dir
        self.file_handler_initialized = (
            False  # Flag to check if file handler has been initialized
        )

        self.logger = logging.getLogger(name)
        self.logger.setLevel(log_level)

        if self.logger.hasHandlers():
            self.logger.handlers.clear()

        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )

        # Create and add console handler
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)

    def _initialize_file_handler(self):
        if not self.file_handler_initialized and self.to_file:
            timestamp = time.strftime("%Y%m%d-%H%M%S", time.gmtime())
            log_dir_path = os.path.join(self.log_dir, "logs")
            if not os.path.exists(log_dir_path):
                os.makedirs(log_dir_path)
            log_file = os.path.join(
                log_dir_path, f"gpf_{__version__}_{self.dataset}_log_{timestamp}.txt"
            )

            file_handler = logging.FileHandler(log_file)
            formatter = logging.Formatter(
                "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            )
            file_handler.setFormatter(formatter)
            file_handler.addFilter(ConsoleOnlyFilter())  # Add filter to file handler
            self.logger.addHandler(file_handler)
            self.file_handler_initialized = True

    def info(self, message, console_only=False):
        if console_only:
            extra = {"console_only": True}
            self.logger.info(message, extra=extra)
        else:
            self._initialize_file_handler()  # Ensure file handler is initialized before writing to it
            self.logger.info(message)

    def warning(self, message):
        self._initialize_file_handler()  # Ensure file handler is initialized before writing to it
        self.logger.warning(message)

    def error(self, message):
        self._initialize_file_handler()  # Ensure file handler is initialized before writing to it
        self.logger.error(message)

    def close(self):
        for handler in self.logger.handlers:
            handler.close()
            self.logger.removeHandler(handler)
