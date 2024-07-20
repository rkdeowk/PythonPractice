from PythonPractice.EC.src.sensors.sensor_interface import ISensor


class Sensor1(ISensor):
    def __init__(self, sensor_id):
        super().__init__(sensor_id)

    def connect(self):
        self._is_connected = True
        self.logger.info(f'connect {self._sensor_id}')

    def disconnect(self):
        self._is_connected = False
        self.logger.info(f'disconnect {self._sensor_id}')

    def is_connected(self):
        return self._is_connected

    def get_data(self):
        if not self._is_connected:
            raise ConnectionError

        data = [1.23, 4.56, 7.89]
        self.logger.info(f'get data {self._sensor_id}, data: {data}')
        return data

    def setting(self, **kwargs):
        self._settings = kwargs
        self.logger.info(f'setting {self._sensor_id} {kwargs.items()}')
