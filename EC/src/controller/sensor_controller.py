from PythonPractice.EC.src.controller.sensor_command import SensorCommand
from PythonPractice.EC.src.sensors.sensor_interface import ISensor


class SensorManager:
    def __init__(self):
        self._sensors: list[ISensor] = []

    def add_sensor(self, sensor: ISensor):
        self._sensors.append(sensor)

    def remove_sensor(self, sensor: ISensor):
        self._sensors.remove(sensor)

    @property
    def sensors(self):
        return self._sensors


class SensorController:
    def __init__(self, sensor_manager: SensorManager):
        self._sensor_manager = sensor_manager

    def execute_command(self, command: SensorCommand):
        return command.execute()
