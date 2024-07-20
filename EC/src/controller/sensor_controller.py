from PythonPractice.EC.src.controller.sensor_command import SensorCommand
from PythonPractice.EC.src.logger.logger import Logger
from PythonPractice.EC.src.sensors.sensor_interface import ISensor


class SensorController:
    def __init__(self):
        self._sensors: list[ISensor] = []
        self.logger = Logger(self.__class__.__name__).get_logger()
        self.logger.info(f'create {self.__class__.__name__}')

    def add_sensor(self, sensor: ISensor):
        self._sensors.append(sensor)
        self.logger.info(f'add sensor {sensor.sensor_id}')

    def remove_sensor(self, sensor: ISensor):
        self._sensors.remove(sensor)
        self.logger.info(f'remove sensor {sensor.sensor_id}')

    def execute_command(self, command: SensorCommand):
        self.logger.info(f'execute command {command.__class__.__name__}')
        return command.execute()

    @property
    def sensor_id_list(self):
        return [sensor.sensor_id for sensor in self._sensors]
