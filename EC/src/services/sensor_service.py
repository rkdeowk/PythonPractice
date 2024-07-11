from PythonPractice.EC.src.controller.sensor_command import SensorCommand
from PythonPractice.EC.src.controller.sensor_controller import SensorManager, SensorController
from PythonPractice.EC.src.sensors.sensor_interface import ISensor


class SensorService:
    def __init__(self, logger):
        self.logger = logger

    def add_sensor(self, manager: SensorManager, sensor: ISensor):
        self.logger.info(f'add sensor: {sensor}')
        manager.add_sensor(sensor)

    def remove_sensor(self, manager: SensorManager, sensor: ISensor):
        self.logger.info(f'remove sensor: {sensor}')
        manager.remove_sensor(sensor)

    def execute_command(self, controller: SensorController, command: SensorCommand):
        self.logger.info(f'execute command: {command}')
        return controller.execute_command(command)
