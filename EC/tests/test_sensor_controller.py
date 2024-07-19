import unittest
from unittest.mock import patch

from src.controller.sensor_command import ConnectSensorCommand, DisconnectSensorCommand, GetDataSensorCommand, \
    IsConnectedSensorCommand, SettingSensorCommand
from src.controller.sensor_controller import SensorController
from src.factory.factory_producer import FactoryProducer
from src.sensors.sensor_type import SensorType

SETTING_PARAM = {
    'arg1': 'value1',
    'arg2': 'value2'
}


class TestSensorController(unittest.TestCase):
    def setUp(self):
        factory_producer = FactoryProducer()
        self.sensor1 = factory_producer.get_factory(SensorType.SENSOR1).create_sensor('1')
        self.sensor2 = factory_producer.get_factory(SensorType.SENSOR2).create_sensor('2')

        self.sensors = [
            ('src.sensors.sensor1.Sensor1', self.sensor1),
            ('src.sensors.sensor2.Sensor2', self.sensor2)
        ]

        self.sensor_controller = SensorController()
        self.sensor_controller.add_sensor(self.sensor1)
        self.sensor_controller.add_sensor(self.sensor2)

    def _test_sensor_controller(self, method_name, test):
        for path, sensor in self.sensors:
            with self.subTest(sensor_type=sensor.__class__.__name__):
                with patch(f'{path}.{method_name}') as mock:
                    test(self.sensor_controller, sensor, mock)

    def test_add_sensor(self):
        self.assertEqual(len(self.sensor_controller._sensors), 2)

    def test_remove_sensor(self):
        self.sensor_controller.remove_sensor(self.sensor2)
        self.assertEqual(len(self.sensor_controller._sensors), 1)
        self.assertEqual(self.sensor_controller._sensors[0], self.sensor1)

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

    def test_sensor_id_list(self):
        self.assertEqual(self.sensor_controller.sensor_id_list, ['1', '2'])


if __name__ == '__main__':
    unittest.main()
