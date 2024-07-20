from PythonPractice.EC.src.factory.factory_abstract import AbstractFactory
from PythonPractice.EC.src.parser.parser_sensor1 import Sensor1Parser
from PythonPractice.EC.src.sensors.sensor1 import Sensor1


class Sensor1Factory(AbstractFactory):
    def create_parser(self):
        self.logger.info(f'create parser {self.__class__.__name__}')
        return Sensor1Parser()

    def create_sensor(self, sensor_id: str):
        self.logger.info(f'create sensor {self.__class__.__name__} {sensor_id}')
        return Sensor1(sensor_id)
