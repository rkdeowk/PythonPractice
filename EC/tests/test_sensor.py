import unittest

from PythonPractice.EC.src.sensors.sensor1 import Sensor1
from PythonPractice.EC.src.sensors.sensor2 import Sensor2
from PythonPractice.EC.src.sensors.sensor3 import Sensor3


class TestSensor(unittest.TestCase):
    def test_sensor1_read_data(self):
        sensor = Sensor1(1)
        self.assertEqual(sensor.read_data(), f"{sensor.__class__.__name__} data from {sensor.id}")

    def test_sensor2_read_data(self):
        sensor = Sensor2(2)
        self.assertEqual(sensor.read_data(), f"{sensor.__class__.__name__} data from {sensor.id}")

    def test_sensor3_read_data(self):
        sensor = Sensor3(3)
        self.assertEqual(sensor.read_data(), f"{sensor.__class__.__name__} data from {sensor.id}")


if __name__ == '__main__':
    unittest.main()
