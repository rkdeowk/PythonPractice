from PythonPractice.EC.src.controller.sensor_command import SensorCommand
from PythonPractice.EC.src.sensors.sensor_interface import ISensor


class SensorController:
    def __init__(self):
        self._sensors: list[ISensor] = []

    def add_sensor(self, sensor: ISensor):
        self._sensors.append(sensor)

    def remove_sensor(self, sensor: ISensor):
        self._sensors.remove(sensor)

    def execute_command(self, command: SensorCommand):
        return command.execute()
