import glob
from implementations.run_list import RunList
from implementations.file_reader import FileReader
from implementations.script_runner import ScriptRunner


class RunListManager:
    def __init__(self):
        self.__file_reader = FileReader()
        self.__script_runner = ScriptRunner()
        self.__run_lists = self.__load_run_lists()
        self.print_run_lists()

    def __load_run_lists(self):
        return [RunList(file_path, self.__file_reader, self.__script_runner) for file_path in
                glob.glob("../script/runlist*.txt")]

    def run(self, run_list_file_name: str):
        run_list = self.__find_run_list(run_list_file_name)
        if run_list:
            print(f"* start : {run_list_file_name}")
            run_list.run()
            print(f"* end   : {run_list_file_name}")

    def run_all(self):
        for run_list in self.__run_lists:
            print(f"* start : {run_list.run_list_file_name}")
            run_list.run()
            print(f"* end   : {run_list.run_list_file_name}")

    def print_run_lists(self):
        for run_list in self.__run_lists:
            print(run_list.run_list_file_name)

    def __find_run_list(self, run_list_file_name: str):
        for run_list in self.__run_lists:
            if run_list.run_list_file_name == run_list_file_name:
                return run_list
        return None
