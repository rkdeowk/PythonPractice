from PythonPractice.EC.src.parser.parser_interface import IParser


class Sensor2Parser(IParser):
    def parse(self, data):
        self.logger.info(f'parse data: {data}')
        return data

    def parse_other_data(self, data):
        self.logger.info(f'parse data: {data}')
        return data
