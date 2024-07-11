from abc import ABC, abstractmethod


class IDataProcessingStrategy(ABC):
    @abstractmethod
    def process_data(self, data, **kwargs):
        pass
