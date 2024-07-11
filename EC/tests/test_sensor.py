import unittest
from unittest.mock import patch

from PythonPractice.EC.src.sensors.sensor_factory import SensorFactory, SensorType

READED_DATA = [1.23, 4.56, 7.89]
SETTING_PARAM = {
    'arg1': 'value1',
    'arg2': 'value2'
}


class TestSensor(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.sensors = [
            ('PythonPractice.EC.src.sensors.sensor1.Sensor1', SensorFactory.create_sensor(SensorType.SENSOR1, '1')),
            ('PythonPractice.EC.src.sensors.sensor2.Sensor2', SensorFactory.create_sensor(SensorType.SENSOR2, '2')),
            ('PythonPractice.EC.src.sensors.sensor3.Sensor3', SensorFactory.create_sensor(SensorType.SENSOR3, '3'))
        ]

    def _test_behavior_sensor_method(self, method_name, test):
        for path, sensor in self.sensors:
            with self.subTest(sensor_type=sensor.__class__.__name__):
                with patch(f'{path}.{method_name}') as mock:
                    test(sensor, mock)

    def test_behavior_sensor_connect(self):
        def test_behavior_connect(sensor, mock):
            sensor.connect()
            mock.assert_called_once()

        self._test_behavior_sensor_method('connect', test_behavior_connect)

    def test_behavior_sensor_disconnect(self):
        def test_behavior_disconnect(sensor, mock):
            sensor.disconnect()
            mock.assert_called_once()

        self._test_behavior_sensor_method('disconnect', test_behavior_disconnect)

    def test_behavior_sensor_is_connected(self):
        def test_behavior_is_connected(sensor, mock):
            sensor.connect()
            sensor.is_connected()
            mock.assert_called_once()

        self._test_behavior_sensor_method('is_connected', test_behavior_is_connected)

    def test_behavior_sensor_get_data(self):
        def test_behavior_get_data(sensor, mock):
            sensor.connect()
            data = sensor.get_data()
            mock.assert_called_once()

        self._test_behavior_sensor_method('get_data', test_behavior_get_data)

    def test_behavior_sensor_get_data_not_connected(self):
        def test_behavior_get_data_not_connected(sensor, mock):
            mock.side_effect = ConnectionError

            sensor.disconnect()
            with self.assertRaises(ConnectionError):
                sensor.get_data()
            mock.assert_called_once()

        self._test_behavior_sensor_method('get_data', test_behavior_get_data_not_connected)

    def test_behavior_sensor_setting(self):
        def test_behavior_setting(sensor, mock):
            sensor.setting(**SETTING_PARAM)
            mock.assert_called_once_with(**SETTING_PARAM)

        self._test_behavior_sensor_method('setting', test_behavior_setting)

    def _test_state_sensor_method(self, test):
        for path, sensor in self.sensors:
            with self.subTest(sensor_type=sensor.__class__.__name__):
                test(sensor)

    def test_state_sensor_connect(self):
        def test_state_connect(sensor):
            sensor.connect()
            self.assertEqual(sensor.is_connected(), True)

        self._test_state_sensor_method(test_state_connect)

    def test_state_sensor_disconnect(self):
        def test_state_disconnect(sensor):
            sensor.disconnect()
            self.assertEqual(sensor.is_connected(), False)

        self._test_state_sensor_method(test_state_disconnect)

    def test_state_sensor_is_connected(self):
        def test_state_is_connected(sensor):
            sensor.connect()
            self.assertEqual(sensor.is_connected(), True)
            sensor.disconnect()
            self.assertEqual(sensor.is_connected(), False)

        self._test_state_sensor_method(test_state_is_connected)

    def test_state_sensor_get_data(self):
        def test_state_get_data(sensor):
            sensor.connect()
            data = sensor.get_data()
            self.assertEqual(data, READED_DATA)

        self._test_state_sensor_method(test_state_get_data)

    def test_state_sensor_get_data_not_connected(self):
        def test_state_get_data_not_connected(sensor):
            sensor.disconnect()
            with self.assertRaises(ConnectionError):
                sensor.get_data()

        self._test_state_sensor_method(test_state_get_data_not_connected)

    def test_state_sensor_setting(self):
        def test_state_setting(sensor):
            sensor.setting(**SETTING_PARAM)
            self.assertEqual(sensor.settings, SETTING_PARAM)

        self._test_state_sensor_method(test_state_setting)


if __name__ == '__main__':
    unittest.main()
