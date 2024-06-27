import unittest

from PythonPractice.EC.src.sensors.sensor1 import Sensor1
from PythonPractice.EC.src.sensors.sensor2 import Sensor2
from PythonPractice.EC.src.sensors.sensor3 import Sensor3


class TestSensor(unittest.TestCase):
    def test_sensor1_connect(self):
        sensor = Sensor1(1)
        self.assertFalse(sensor.connected)
        result = sensor.connect()
        self.assertTrue(sensor.connected)
        self.assertEqual(result, "Sensor 1 connected.")

    def test_sensor1_disconnect(self):
        sensor = Sensor1(1)
        sensor.connect()
        result = sensor.disconnect()
        self.assertFalse(sensor.connected)
        self.assertEqual(result, "Sensor 1 disconnected.")

    def test_sensor1_read_data(self):
        sensor = Sensor1(1)
        sensor.connect()
        data = sensor.read_data()
        self.assertEqual(data, "Sensor1 data from 1")

    def test_sensor1_read_data_not_connected(self):
        sensor = Sensor1(1)
        with self.assertRaises(ConnectionError):
            sensor.read_data()

    def test_sensor1_setting(self):
        sensor = Sensor1(1)
        settings = {"sensitivity": 10, "range": 100}
        result = sensor.setting(**settings)
        self.assertEqual(sensor.settings, settings)
        self.assertEqual(result, f"Sensor 1 settings updated: {settings}")

    def test_sensor2_connect(self):
        pass

    def test_sensor2_disconnect(self):
        pass

    def test_sensor2_read_data(self):
        pass

    def test_sensor2_read_data_not_connected(self):
        pass

    def test_sensor2_setting(self):
        pass

    def test_sensor3_connect(self):
        pass

    def test_sensor3_disconnect(self):
        pass

    def test_sensor3_read_data(self):
        pass

    def test_sensor3_read_data_not_connected(self):
        pass

    def test_sensor3_setting(self):
        pass


if __name__ == '__main__':
    unittest.main()
