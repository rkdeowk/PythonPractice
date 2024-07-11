import unittest
from unittest.mock import patch

from PythonPractice.EC.src.controller.sensor_command import ConnectSensorCommand, DisconnectSensorCommand, \
    IsConnectedSensorCommand, GetDataSensorCommand, SettingSensorCommand
from PythonPractice.EC.src.controller.sensor_controller import SensorController
from PythonPractice.EC.src.sensors.sensor_factory import SensorFactory, SensorType

SETTING_PARAM = {
    'arg1': 'value1',
    'arg2': 'value2'
}


class TestSensorController(unittest.TestCase):
    def setUp(self):
        self.sensors = [
            ('src.sensors.sensor1.Sensor1', SensorFactory.create_sensor(SensorType.SENSOR1, '1')),
            ('src.sensors.sensor2.Sensor2', SensorFactory.create_sensor(SensorType.SENSOR2, '2')),
            ('src.sensors.sensor3.Sensor3', SensorFactory.create_sensor(SensorType.SENSOR3, '3'))
        ]

        self.sensor_controller = SensorController()
        self.sensor_controller.add_sensor(self.sensors[0][1])
        self.sensor_controller.add_sensor(self.sensors[1][1])
        self.sensor_controller.add_sensor(self.sensors[2][1])

    def _test_sensor_controller(self, method_name, test):
        for path, sensor in self.sensors:
            with self.subTest(sensor_type=sensor.__class__.__name__):
                with patch(f'{path}.{method_name}') as mock:
                    test(self.sensor_controller, sensor, mock)

    def test_add_sensor(self):
        self.assertEqual(len(self.sensor_controller._sensors), 3)

    def test_remove_sensor(self):
        self.sensor_controller.remove_sensor(self.sensors[1][1])
        self.sensor_controller.remove_sensor(self.sensors[2][1])
        self.assertEqual(len(self.sensor_controller._sensors), 1)
        self.assertEqual(self.sensor_controller._sensors[0], self.sensors[0][1])

    def test_connect_sensor(self):
        def test_connect(sensor_controller, sensor, mock):
            sensor_controller.execute_command(ConnectSensorCommand(sensor))
            mock.assert_called_once()

        self._test_sensor_controller('connect', test_connect)

    def test_disconnect_sensor(self):
        def test_disconnect(sensor_controller, sensor, mock):
            sensor_controller.execute_command(DisconnectSensorCommand(sensor))
            mock.assert_called_once()

        self._test_sensor_controller('disconnect', test_disconnect)

    def test_is_connected_sensor(self):
        def test_is_connected(sensor_controller, sensor, mock):
            sensor_controller.execute_command(IsConnectedSensorCommand(sensor))
            mock.assert_called_once()

        self._test_sensor_controller('is_connected', test_is_connected)

    def test_get_data_sensor(self):
        def test_get_data(sensor_controller, sensor, mock):
            sensor_controller.execute_command(ConnectSensorCommand(sensor))
            sensor_controller.execute_command(GetDataSensorCommand(sensor))
            mock.assert_called_once()

        self._test_sensor_controller('get_data', test_get_data)

    def test_setting_sensor(self):
        def test_setting(sensor_controller, sensor, mock):
            sensor_controller.execute_command(SettingSensorCommand(sensor, **SETTING_PARAM))
            mock.assert_called_once_with(**SETTING_PARAM)

        self._test_sensor_controller('setting', test_setting)


if __name__ == '__main__':
    unittest.main()
