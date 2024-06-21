from PythonPractice.run_list.src.interfaces.file_reader_interface import FileReaderInterface


class FileReader(FileReaderInterface):
    def read(self, file_path: str):
        with open(file_path, "r") as file:
            return file.read().splitlines()
