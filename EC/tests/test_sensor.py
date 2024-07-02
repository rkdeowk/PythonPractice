import unittest
from unittest.mock import patch

from PythonPractice.EC.src.sensors.sensor1 import Sensor1
from PythonPractice.EC.src.sensors.sensor2 import Sensor2
from PythonPractice.EC.src.sensors.sensor3 import Sensor3

SAMPLE_DATA = [1.23, 4.56, 7.89]


class TestSensor(unittest.TestCase):
    def setUp(self):
        self.sensors = [
            ('PythonPractice.EC.src.sensors.sensor1.Sensor1', Sensor1(id=1)),
            ('PythonPractice.EC.src.sensors.sensor2.Sensor2', Sensor2(id=2)),
            ('PythonPractice.EC.src.sensors.sensor3.Sensor3', Sensor3(id=3))
        ]

    def test_sensor_connect(self):
        self._test_sensor_method('connect')

    def test_sensor_disconnect(self):
        self._test_sensor_method('disconnect')

    def test_sensor_is_connected(self):
        self._test_sensor_method('is_connected', return_value=True, assertion=self.assertTrue)

    def test_sensor_read_data(self):
        self._test_sensor_method('read_data', return_value=SAMPLE_DATA,
                                 assertion=lambda x: self.assertEqual(x, SAMPLE_DATA))

    def test_sensor_setting(self):
        self._test_sensor_method('setting', call_args={'param': 'value'})

    def _test_sensor_method(self, method_name, return_value=None, assertion=None, call_args=None):
        for path, sensor in self.sensors:
            sensor_type = sensor.__class__.__name__
            with self.subTest(sensor_type=sensor_type):
                self._run_single_sensor_test(path, sensor, method_name, return_value, assertion, call_args)

    def _run_single_sensor_test(self, path, sensor, method_name, return_value, assertion, call_args):
        with self._patch_sensor_method(path, method_name, return_value) as mock_method:
            result = self._call_sensor_method(sensor, method_name, call_args)
            self._verify_method_call(mock_method, call_args)
            self._run_assertion(assertion, result)

    def _patch_sensor_method(self, path, method_name, return_value):
        return patch(f'{path}.{method_name}', return_value=return_value)

    def _call_sensor_method(self, sensor, method_name, call_args):
        method = getattr(sensor, method_name)
        return method(**call_args or {})

    def _verify_method_call(self, mock_method, call_args):
        if call_args:
            mock_method.assert_called_once_with(**call_args)
        else:
            mock_method.assert_called_once()

    def _run_assertion(self, assertion, result):
        if assertion:
            assertion(result)


if __name__ == '__main__':
    unittest.main()
