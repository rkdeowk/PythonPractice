import unittest
from unittest.mock import patch

from PythonPractice.EC.src.sensors.sensor1 import Sensor1
from PythonPractice.EC.src.sensors.sensor2 import Sensor2
from PythonPractice.EC.src.sensors.sensor3 import Sensor3


class TestSensor(unittest.TestCase):
    @patch('PythonPractice.EC.src.sensors.sensor1.Sensor1.connect')
    def test_sensor1_connect(self, mock_connect):
        sensor = Sensor1(id=1)
        sensor.connect()
        mock_connect.assert_called_once()

    @patch('PythonPractice.EC.src.sensors.sensor1.Sensor1.disconnect')
    def test_sensor1_disconnect(self, mock_disconnect):
        sensor = Sensor1(id=1)
        sensor.disconnect()
        mock_disconnect.assert_called_once()

    @patch('PythonPractice.EC.src.sensors.sensor1.Sensor1.is_connected', return_value=True)
    def test_sensor1_is_connected(self, mock_is_connected):
        sensor = Sensor1(id=1)
        self.assertTrue(sensor.is_connected())
        mock_is_connected.assert_called_once()

    @patch('PythonPractice.EC.src.sensors.sensor1.Sensor1.read_data', return_value=[1.23, 4.56, 7.89])
    def test_sensor1_read_data(self, mock_read_data):
        sensor = Sensor1(id=1)
        data = sensor.read_data()
        self.assertEqual(data, [1.23, 4.56, 7.89])
        mock_read_data.assert_called_once()

    @patch('PythonPractice.EC.src.sensors.sensor1.Sensor1.is_connected', return_value=False)
    def test_sensor1_read_data_not_connected(self, mock_is_connected):
        sensor = Sensor1(id=1)
        with self.assertRaises(ConnectionError):
            sensor.read_data()
        mock_is_connected.assert_called_once()

    @patch('PythonPractice.EC.src.sensors.sensor1.Sensor1.setting')
    def test_sensor1_setting(self, mock_setting):
        sensor = Sensor1(id=1)
        sensor.setting(param='value')
        mock_setting.assert_called_once_with(param='value')

    @patch('PythonPractice.EC.src.sensors.sensor2.Sensor2.connect')
    def test_sensor2_connect(self, mock_connect):
        sensor = Sensor2(id=1)
        sensor.connect()
        mock_connect.assert_called_once()

    @patch('PythonPractice.EC.src.sensors.sensor2.Sensor2.disconnect')
    def test_sensor2_disconnect(self, mock_disconnect):
        sensor = Sensor2(id=1)
        sensor.disconnect()
        mock_disconnect.assert_called_once()

    @patch('PythonPractice.EC.src.sensors.sensor2.Sensor2.is_connected', return_value=True)
    def test_sensor2_is_connected(self, mock_is_connected):
        sensor = Sensor2(id=1)
        self.assertTrue(sensor.is_connected())
        mock_is_connected.assert_called_once()

    @patch('PythonPractice.EC.src.sensors.sensor2.Sensor2.read_data', return_value=[1.23, 4.56, 7.89])
    def test_sensor2_read_data(self, mock_read_data):
        sensor = Sensor2(id=1)
        data = sensor.read_data()
        self.assertEqual(data, [1.23, 4.56, 7.89])
        mock_read_data.assert_called_once()

    @patch('PythonPractice.EC.src.sensors.sensor2.Sensor2.is_connected', return_value=False)
    def test_sensor2_read_data_not_connected(self, mock_is_connected):
        sensor = Sensor2(id=1)
        with self.assertRaises(ConnectionError):
            sensor.read_data()
        mock_is_connected.assert_called_once()

    @patch('PythonPractice.EC.src.sensors.sensor2.Sensor2.setting')
    def test_sensor2_setting(self, mock_setting):
        sensor = Sensor2(id=1)
        sensor.setting(param='value')
        mock_setting.assert_called_once_with(param='value')

    @patch('PythonPractice.EC.src.sensors.sensor3.Sensor3.connect')
    def test_sensor3_connect(self, mock_connect):
        sensor = Sensor3(id=1)
        sensor.connect()
        mock_connect.assert_called_once()

    @patch('PythonPractice.EC.src.sensors.sensor3.Sensor3.disconnect')
    def test_sensor3_disconnect(self, mock_disconnect):
        sensor = Sensor3(id=1)
        sensor.disconnect()
        mock_disconnect.assert_called_once()

    @patch('PythonPractice.EC.src.sensors.sensor3.Sensor3.is_connected', return_value=True)
    def test_sensor3_is_connected(self, mock_is_connected):
        sensor = Sensor3(id=1)
        self.assertTrue(sensor.is_connected())
        mock_is_connected.assert_called_once()

    @patch('PythonPractice.EC.src.sensors.sensor3.Sensor3.read_data', return_value=[1.23, 4.56, 7.89])
    def test_sensor3_read_data(self, mock_read_data):
        sensor = Sensor3(id=1)
        data = sensor.read_data()
        self.assertEqual(data, [1.23, 4.56, 7.89])
        mock_read_data.assert_called_once()

    @patch('PythonPractice.EC.src.sensors.sensor3.Sensor3.is_connected', return_value=False)
    def test_sensor3_read_data_not_connected(self, mock_is_connected):
        sensor = Sensor3(id=1)
        with self.assertRaises(ConnectionError):
            sensor.read_data()
        mock_is_connected.assert_called_once()

    @patch('PythonPractice.EC.src.sensors.sensor3.Sensor3.setting')
    def test_sensor3_setting(self, mock_setting):
        sensor = Sensor3(id=1)
        sensor.setting(param='value')
        mock_setting.assert_called_once_with(param='value')


if __name__ == '__main__':
    unittest.main()
