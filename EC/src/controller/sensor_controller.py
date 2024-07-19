from src.controller.sensor_command import SensorCommand
from src.sensors.sensor_interface import ISensor


class SensorController:
    def __init__(self):
        self._sensors: list[ISensor] = []

    def add_sensor(self, sensor: ISensor):
        self._sensors.append(sensor)

    def remove_sensor(self, sensor: ISensor):
        self._sensors.remove(sensor)

    def execute_command(self, command: SensorCommand):
        return command.execute()

    @property
    def sensor_id_list(self):
        return [sensor.sensor_id for sensor in self._sensors]
