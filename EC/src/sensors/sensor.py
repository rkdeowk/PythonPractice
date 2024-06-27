from abc import ABC, abstractmethod


class Sensor(ABC):
    def __init__(self, id):
        self.id = id
        self.connected = False
        self.settings = {}

    @abstractmethod
    def connect(self):
        raise NotImplementedError(f"{self.__class__.__name__} must implement connect method")

    @abstractmethod
    def disconnect(self):
        raise NotImplementedError(f"{self.__class__.__name__} must implement disconnect method")

    @abstractmethod
    def read_data(self):
        if not self.connected:
            raise ConnectionError(f"Sensor {self.id} is not connected.")
        raise NotImplementedError(f"{self.__class__.__name__} must implement read_data method")

    @abstractmethod
    def setting(self, **kwargs):
        raise NotImplementedError(f"{self.__class__.__name__} must implement setting method")
