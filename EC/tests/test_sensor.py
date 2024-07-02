import unittest
from unittest.mock import patch
from PythonPractice.EC.src.sensors.sensor1 import Sensor1
from PythonPractice.EC.src.sensors.sensor2 import Sensor2
from PythonPractice.EC.src.sensors.sensor3 import Sensor3

READED_DATA = [1.23, 4.56, 7.89]


class TestSensor(unittest.TestCase):
    def setUp(self):
        self.sensors = [
            ('PythonPractice.EC.src.sensors.sensor1.Sensor1', Sensor1(id=1)),
            ('PythonPractice.EC.src.sensors.sensor2.Sensor2', Sensor2(id=2)),
            ('PythonPractice.EC.src.sensors.sensor3.Sensor3', Sensor3(id=3))
        ]

    def test_sensor_connect(self):
        for path, sensor in self.sensors:
            with patch(f'{path}.connect') as mock_connect:
                sensor.connect()
                mock_connect.assert_called_once()

    def test_sensor_disconnect(self):
        for path, sensor in self.sensors:
            with patch(f'{path}.disconnect') as mock_disconnect:
                sensor.disconnect()
                mock_disconnect.assert_called_once()

    def test_sensor_is_connected(self):
        for path, sensor in self.sensors:
            with patch(f'{path}.is_connected', return_value=True) as mock_is_connected:
                self.assertTrue(sensor.is_connected())
                mock_is_connected.assert_called_once()

    def test_sensor_read_data(self):
        for path, sensor in self.sensors:
            with patch(f'{path}.read_data', return_value=READED_DATA) as mock_read_data:
                data = sensor.read_data()
                self.assertEqual(data, READED_DATA)
                mock_read_data.assert_called_once()

    def test_sensor_setting(self):
        for path, sensor in self.sensors:
            with patch(f'{path}.setting') as mock_setting:
                sensor.setting(param='value')
                mock_setting.assert_called_once_with(param='value')


if __name__ == '__main__':
    unittest.main()
