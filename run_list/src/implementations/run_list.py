from pathlib import Path

from PythonPractice.run_list.src.constant import FAIL
from PythonPractice.run_list.src.interfaces.file_reader_interface import FileReaderInterface
from PythonPractice.run_list.src.interfaces.run_list_interface import RunListInterface
from PythonPractice.run_list.src.interfaces.script_runner_interface import ScriptRunnerInterface


class RunList(RunListInterface):
    def __init__(self, run_list_file_path: str, file_reader: FileReaderInterface, script_runner: ScriptRunnerInterface):
        self.__run_list_file_path = run_list_file_path
        self.__file_reader = file_reader
        self.__script_runner = script_runner

    def run(self):
        script_paths = self.__file_reader.read(self.__run_list_file_path)
        for i, script_path in enumerate(script_paths):
            returncode, script_name = self.__script_runner.run_script(script_path)
            if returncode == FAIL:
                print(f"** fail : {i:>2} {script_name}")
            else:
                print(f"** pass : {i:>2} {script_name}")

    @property
    def run_list_file_name(self):
        return Path(self.__run_list_file_path).name
