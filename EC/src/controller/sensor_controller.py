from PythonPractice.EC.src.data_processor.data_processor import DataProcessor
from PythonPractice.EC.src.sensors.sensor1 import Sensor1
from PythonPractice.EC.src.sensors.sensor2 import Sensor2
from PythonPractice.EC.src.sensors.sensor3 import Sensor3


class SensorController:
    def __init__(self):
        self.sensors = [Sensor1(1), Sensor2(2), Sensor3(3)]
        self.processor = DataProcessor()

    def collect_and_process_data(self):
        for sensor in self.sensors:
            sensor.connect()
            sensor.setting(sensitivity=10, range=100)
            data = sensor.read_data()
            processed_data = self.processor.process(data)
            self.display(processed_data)
            sensor.disconnect()

    def display(self, data):
        print(data)
