from src.factory.factory_abstract import AbstractFactory
from src.parser.parser_sensor2 import Sensor2Parser
from src.sensors.sensor2 import Sensor2


class Sensor2Factory(AbstractFactory):
    def create_parser(self):
        return Sensor2Parser()

    def create_sensor(self, sensor_id: str):
        return Sensor2(sensor_id)
