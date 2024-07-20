from abc import ABC, abstractmethod

from PythonPractice.EC.src.logger.logger import Logger


class AbstractFactory(ABC):
    def __init__(self):
        self.logger = Logger(self.__class__.__name__).get_logger()
        self.logger.info(f'create {self.__class__.__name__}')

    @abstractmethod
    def create_parser(self):
        pass

    @abstractmethod
    def create_sensor(self, sensor_id: str):
        pass
