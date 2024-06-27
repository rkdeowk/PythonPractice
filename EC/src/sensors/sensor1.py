from PythonPractice.EC.src.sensors.sensor import Sensor


class Sensor1(Sensor):
    def connect(self):
        self.connected = True
        return f"Sensor {self.id} connected."

    def disconnect(self):
        self.connected = False
        return f"Sensor {self.id} disconnected."

    def read_data(self):
        if not self.connected:
            raise ConnectionError(f"Sensor {self.id} is not connected.")
        return f"Sensor1 data from {self.id}"

    def setting(self, **kwargs):
        self.settings.update(kwargs)
        return f"Sensor {self.id} settings updated: {self.settings}"
