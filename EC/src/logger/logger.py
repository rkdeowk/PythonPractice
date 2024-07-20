import logging
import os
from logging.handlers import RotatingFileHandler


class Logger:
    def __init__(self, class_name: str, log_dir: str = '../logs', log_file: str = 'app.log', level: int = logging.INFO):
        self.logger = self._initialize_logger(class_name, level)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # class_log_dir = self._prepare_directory(log_dir, class_name)
        # file_handler = self._create_file_handler(class_log_dir, log_file, formatter)

        full_log_dir = self._prepare_directory(log_dir, 'full_log')
        full_log_handler = self._create_file_handler(full_log_dir, 'full.log', formatter)

        console_handler = self._create_console_handler(formatter)

        self._add_handlers(full_log_handler, console_handler)

    def _initialize_logger(self, class_name: str, level: int) -> logging.Logger:
        logger = logging.getLogger(class_name)
        logger.setLevel(level)
        return logger

    def _prepare_directory(self, base_dir: str, sub_dir: str) -> str:
        directory = os.path.join(base_dir, sub_dir)
        os.makedirs(directory, exist_ok=True)
        return directory

    def _create_file_handler(self, dir_path: str, file_name: str, formatter: logging.Formatter,
                             max_bytes: int = 5 * 1024 * 1024, backup_count: int = 20) -> RotatingFileHandler:
        file_path = os.path.join(dir_path, file_name)
        file_handler = RotatingFileHandler(file_path, maxBytes=max_bytes, backupCount=backup_count)
        file_handler.setFormatter(formatter)
        return file_handler

    def _create_console_handler(self, formatter: logging.Formatter) -> logging.StreamHandler:
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        return console_handler

    def _add_handlers(self, *handlers: logging.Handler) -> None:
        for handler in handlers:
            self.logger.addHandler(handler)

    def get_logger(self) -> logging.Logger:
        return self.logger
