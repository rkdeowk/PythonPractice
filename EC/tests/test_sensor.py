import unittest
from unittest.mock import patch

from PythonPractice.EC.src.sensors.sensor1 import Sensor1
from PythonPractice.EC.src.sensors.sensor2 import Sensor2
from PythonPractice.EC.src.sensors.sensor3 import Sensor3

READED_DATA = [1.23, 4.56, 7.89]


class TestSensor(unittest.TestCase):
    def setUp(self):
        self.sensor1 = Sensor1(id=1)
        self.sensor2 = Sensor2(id=2)
        self.sensor3 = Sensor3(id=3)

    @patch('PythonPractice.EC.src.sensors.sensor1.Sensor1.connect')
    def test_sensor1_connect(self, mock_connect):
        self.sensor1.connect()
        mock_connect.assert_called_once()

    @patch('PythonPractice.EC.src.sensors.sensor1.Sensor1.disconnect')
    def test_sensor1_disconnect(self, mock_disconnect):
        self.sensor1.disconnect()
        mock_disconnect.assert_called_once()

    @patch('PythonPractice.EC.src.sensors.sensor1.Sensor1.is_connected', return_value=True)
    def test_sensor1_is_connected(self, mock_is_connected):
        self.assertTrue(self.sensor1.is_connected())
        mock_is_connected.assert_called_once()

    @patch('PythonPractice.EC.src.sensors.sensor1.Sensor1.read_data', return_value=READED_DATA)
    def test_sensor1_read_data(self, mock_read_data):
        data = self.sensor1.read_data()
        self.assertEqual(data, READED_DATA)
        mock_read_data.assert_called_once()

    @patch('PythonPractice.EC.src.sensors.sensor1.Sensor1.setting')
    def test_sensor1_setting(self, mock_setting):
        self.sensor1.setting(param='value')
        mock_setting.assert_called_once_with(param='value')

    @patch('PythonPractice.EC.src.sensors.sensor2.Sensor2.connect')
    def test_sensor2_connect(self, mock_connect):
        self.sensor2.connect()
        mock_connect.assert_called_once()

    @patch('PythonPractice.EC.src.sensors.sensor2.Sensor2.disconnect')
    def test_sensor2_disconnect(self, mock_disconnect):
        self.sensor2.disconnect()
        mock_disconnect.assert_called_once()

    @patch('PythonPractice.EC.src.sensors.sensor2.Sensor2.is_connected', return_value=True)
    def test_sensor2_is_connected(self, mock_is_connected):
        self.assertTrue(self.sensor2.is_connected())
        mock_is_connected.assert_called_once()

    @patch('PythonPractice.EC.src.sensors.sensor2.Sensor2.read_data', return_value=READED_DATA)
    def test_sensor2_read_data(self, mock_read_data):
        data = self.sensor2.read_data()
        self.assertEqual(data, READED_DATA)
        mock_read_data.assert_called_once()

    @patch('PythonPractice.EC.src.sensors.sensor2.Sensor2.setting')
    def test_sensor2_setting(self, mock_setting):
        self.sensor2.setting(param='value')
        mock_setting.assert_called_once_with(param='value')

    @patch('PythonPractice.EC.src.sensors.sensor3.Sensor3.connect')
    def test_sensor3_connect(self, mock_connect):
        self.sensor3.connect()
        mock_connect.assert_called_once()

    @patch('PythonPractice.EC.src.sensors.sensor3.Sensor3.disconnect')
    def test_sensor3_disconnect(self, mock_disconnect):
        self.sensor3.disconnect()
        mock_disconnect.assert_called_once()

    @patch('PythonPractice.EC.src.sensors.sensor3.Sensor3.is_connected', return_value=True)
    def test_sensor3_is_connected(self, mock_is_connected):
        self.assertTrue(self.sensor3.is_connected())
        mock_is_connected.assert_called_once()

    @patch('PythonPractice.EC.src.sensors.sensor3.Sensor3.read_data', return_value=READED_DATA)
    def test_sensor3_read_data(self, mock_read_data):
        data = self.sensor3.read_data()
        self.assertEqual(data, READED_DATA)
        mock_read_data.assert_called_once()

    @patch('PythonPractice.EC.src.sensors.sensor3.Sensor3.setting')
    def test_sensor3_setting(self, mock_setting):
        self.sensor3.setting(param='value')
        mock_setting.assert_called_once_with(param='value')


if __name__ == '__main__':
    unittest.main()
