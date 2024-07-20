from PythonPractice.EC.src.factory.factory_abstract import AbstractFactory
from PythonPractice.EC.src.parser.parser_sensor2 import Sensor2Parser
from PythonPractice.EC.src.sensors.sensor2 import Sensor2


class Sensor2Factory(AbstractFactory):
    def create_parser(self):
        self.logger.info(f'create parser {self.__class__.__name__}')
        return Sensor2Parser()

    def create_sensor(self, sensor_id: str):
        self.logger.info(f'create sensor {self.__class__.__name__} {sensor_id}')
        return Sensor2(sensor_id)
