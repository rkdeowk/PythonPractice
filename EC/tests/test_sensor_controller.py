import unittest
from unittest.mock import patch, MagicMock, Mock
from PythonPractice.EC.src.controller.sensor_controller import SensorController
from PythonPractice.EC.src.data_processor.data_processor import DataProcessor
from PythonPractice.EC.src.sensors.sensor1 import Sensor1
from PythonPractice.EC.src.sensors.sensor2 import Sensor2
from PythonPractice.EC.src.sensors.sensor3 import Sensor3


class TestSensorController(unittest.TestCase):
    def test_collect_and_process_data(self):
        mock_sensor1 = Mock(Sensor1)
        mock_sensor2 = Mock(Sensor2)
        mock_sensor3 = Mock(Sensor3)
        mock_data_processor = Mock(DataProcessor)

        mock_sensor1.connect = MagicMock()
        mock_sensor1.disconnect = MagicMock()
        mock_sensor1.read_data.return_value = [1.0, 2.0, 3.0]

        mock_sensor2.connect = MagicMock()
        mock_sensor2.disconnect = MagicMock()
        mock_sensor2.read_data.return_value = [4.0, 5.0, 6.0]

        mock_sensor3.connect = MagicMock()
        mock_sensor3.disconnect = MagicMock()
        mock_sensor3.read_data.return_value = [7.0, 8.0, 9.0]

        mock_data_processor.process.side_effect = lambda data: sum(data)

        controller = Mock(SensorController)

        controller.sensors = [mock_sensor1, mock_sensor2, mock_sensor3]
        controller.data_processor = mock_data_processor

        mock_sensor1.connect()
        mock_sensor2.connect()
        mock_sensor3.connect()

        controller.collect_and_process_data()

        mock_sensor1.read_data()
        mock_sensor2.read_data()
        mock_sensor3.read_data()

        mock_data_processor.process([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0])

        mock_sensor1.disconnect()
        mock_sensor2.disconnect()
        mock_sensor3.disconnect()

        # assert
        mock_sensor1.connect.assert_called_once()
        mock_sensor2.connect.assert_called_once()
        mock_sensor3.connect.assert_called_once()

        mock_sensor1.read_data.assert_called_once()
        mock_sensor2.read_data.assert_called_once()
        mock_sensor3.read_data.assert_called_once()

        mock_data_processor.process.assert_called_once_with([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0])

        mock_sensor1.disconnect.assert_called_once()
        mock_sensor2.disconnect.assert_called_once()
        mock_sensor3.disconnect.assert_called_once()


if __name__ == '__main__':
    unittest.main()
