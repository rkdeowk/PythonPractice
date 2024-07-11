from PythonPractice.EC.src.parser.parser_interface import IParser


class XmlParser(IParser):
    def parse(self, data):
        print(f'parsing data in XML format: {data}')
