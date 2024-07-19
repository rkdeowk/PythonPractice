from src.sensors.sensor_interface import ISensor


class Sensor1(ISensor):
    def __init__(self, sensor_id):
        super().__init__(sensor_id)

    def connect(self):
        self._is_connected = True

    def disconnect(self):
        self._is_connected = False

    def is_connected(self):
        return self._is_connected

    def get_data(self):
        if not self._is_connected:
            raise ConnectionError
        return [1.23, 4.56, 7.89]

    def setting(self, **kwargs):
        self._settings = kwargs
