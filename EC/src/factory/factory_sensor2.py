from PythonPractice.EC.src.factory.factory_abstract import AbstractFactory
from PythonPractice.EC.src.parser.parser_sensor2 import Sensor2Parser
from PythonPractice.EC.src.sensors.sensor2 import Sensor2


class Sensor2Factory(AbstractFactory):
    def create_parser(self):
        return Sensor2Parser()

    def create_sensor(self, sensor_id: str):
        return Sensor2(sensor_id)
