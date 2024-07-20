from PythonPractice.EC.src.parser.parser_interface import IParser


class Sensor2Parser(IParser):
    def parse(self, data):
        return data

    def parse_other_data(self, data):
        return data
