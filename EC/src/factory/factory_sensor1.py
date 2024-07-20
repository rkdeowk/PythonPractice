from PythonPractice.EC.src.factory.factory_abstract import AbstractFactory
from PythonPractice.EC.src.parser.parser_sensor1 import Sensor1Parser
from PythonPractice.EC.src.sensors.sensor1 import Sensor1


class Sensor1Factory(AbstractFactory):
    def create_parser(self):
        return Sensor1Parser()

    def create_sensor(self, sensor_id: str):
        return Sensor1(sensor_id)
