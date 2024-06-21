from abc import ABC, abstractmethod


class ScriptRunnerInterface(ABC):
    @abstractmethod
    def run_script(self, script_name: str):
        pass
