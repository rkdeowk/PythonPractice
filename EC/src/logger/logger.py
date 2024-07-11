import logging
from datetime import datetime
from logging.handlers import TimedRotatingFileHandler

from PythonPractice.EC.src.di_container import DIContainer


class Logger:
    def __init__(self, name: str, level=logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)

        log_file = f'{datetime.now().strftime('%Y-%m-%d')}_{name}.log'
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        file_handler = TimedRotatingFileHandler(log_file, when='midnight', interval=1, backupCount=0)
        file_handler.setFormatter(formatter)

        self.logger.addHandler(console_handler)
        self.logger.addHandler(file_handler)

    def get_logger(self):
        return self.logger


container = DIContainer()
container.register('Logger', Logger('AppLoger').get_logger())
