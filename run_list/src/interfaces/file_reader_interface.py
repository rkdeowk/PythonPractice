from abc import ABC, abstractmethod


class FileReaderInterface(ABC):
    @abstractmethod
    def read(self, file_path: str):
        pass
