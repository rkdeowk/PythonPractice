from abc import ABC, abstractmethod


class Sensor(ABC):
    def __init__(self, id):
        self.id = id

    @abstractmethod
    def read_data(self):
        raise NotImplementedError
