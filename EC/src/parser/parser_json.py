from src.parser.parser_interface import IParser


class JsonParser(IParser):
    def parse(self, data):
        print(f'parsing data in JSON format: {data}')
