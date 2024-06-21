from abc import ABC, abstractmethod


class RunListInterface(ABC):
    @abstractmethod
    def run(self):
        pass

    @property
    @abstractmethod
    def run_list_file_name(self):
        pass
