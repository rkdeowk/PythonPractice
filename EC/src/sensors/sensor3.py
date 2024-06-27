from PythonPractice.EC.src.sensors.sensor import Sensor


class Sensor3(Sensor):
    def read_data(self):
        return f"Sensor3 data from {self.id}"
