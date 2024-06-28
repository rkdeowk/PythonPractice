from PythonPractice.EC.src.sensors.sensor import Sensor


class Sensor2(Sensor):
    def connect(self):
        pass

    def disconnect(self):
        pass

    def is_connected(self):
        pass

    def read_data(self):
        if not self.is_connected():
            raise ConnectionError(f"Sensor {self.id} is not connected.")
        pass

    def setting(self, **kwargs):
        self.settings.update(kwargs)
        pass
