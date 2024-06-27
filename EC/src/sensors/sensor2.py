from PythonPractice.EC.src.sensors.sensor import Sensor


class Sensor2(Sensor):
    def read_data(self):
        return f"Sensor2 data from {self.id}"
