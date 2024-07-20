from abc import ABC, abstractmethod

from PythonPractice.EC.src.logger.logger import Logger


class ISensor(ABC):
    def __init__(self, sensor_id: str):
        self._sensor_id = sensor_id
        self._settings = {}
        self._is_connected = False
        self.logger = Logger(self.__class__.__name__).get_logger()
        self.logger.info(f'create {self.__class__.__name__}')

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass

    @abstractmethod
    def is_connected(self):
        pass

    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def setting(self, **kwargs):
        pass

    @property
    def sensor_id(self):
        return self._sensor_id

    @property
    def settings(self):
        return self._settings
