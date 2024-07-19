from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    @abstractmethod
    def create_parser(self):
        pass

    @abstractmethod
    def create_sensor(self, sensor_id: str):
        pass
