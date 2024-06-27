from PythonPractice.EC.src.sensors.sensor import Sensor


class Sensor1(Sensor):
    def read_data(self):
        return f"Sensor1 data from {self.id}"
