from abc import ABC, abstractmethod

from PythonPractice.EC.src.sensors.sensor_interface import ISensor


class SensorCommand(ABC):
    def __init__(self, sensor: ISensor):
        self._sensor = sensor

    @abstractmethod
    def execute(self):
        pass


class ConnectSensorCommand(SensorCommand):
    def execute(self):
        self._sensor.connect()


class DisconnectSensorCommand(SensorCommand):
    def execute(self):
        self._sensor.disconnect()


class IsConnectedSensorCommand(SensorCommand):
    def execute(self):
        return self._sensor.is_connected()


class GetDataSensorCommand(SensorCommand):
    def execute(self):
        return self._sensor.get_data()


class SettingSensorCommand(SensorCommand):
    def __init__(self, sensor: ISensor, **kwargs):
        super().__init__(sensor)
        self._settings = kwargs

    def execute(self):
        self._sensor.setting(**self._settings)
