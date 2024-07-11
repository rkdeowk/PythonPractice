from abc import ABC, abstractmethod


class ISensor(ABC):
    def __init__(self, sensor_id: str):
        self._sensor_id = sensor_id
        self._settings = {}
        self._is_connected = False

    @abstractmethod
    def connect(self):
        raise NotImplementedError(f"{self.__class__.__name__} must implement connect method")

    @abstractmethod
    def disconnect(self):
        raise NotImplementedError(f"{self.__class__.__name__} must implement disconnect method")

    @abstractmethod
    def is_connected(self):
        raise NotImplementedError(f"{self.__class__.__name__} must implement is_connected method")

    @abstractmethod
    def get_data(self):
        if not self.is_connected:
            raise ConnectionError(f"Sensor {self._sensor_id} is not connected.")
        raise NotImplementedError(f"{self.__class__.__name__} must implement read_data method")

    @abstractmethod
    def setting(self, **kwargs):
        raise NotImplementedError(f"{self.__class__.__name__} must implement setting method")

    @property
    def sensor_id(self):
        return self._sensor_id

    @property
    def settings(self):
        return self._settings
