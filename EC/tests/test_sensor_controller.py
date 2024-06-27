import unittest
from unittest.mock import patch

from PythonPractice.EC.src.controller.sensor_controller import SensorController


class TestSensorController(unittest.TestCase):
    @patch('builtins.print')
    def test_collect_and_process_data(self, mock_print):
        controller = SensorController()
        controller.collect_and_process_data()
        self.assertEqual(mock_print.call_count, 3)
        mock_print.assert_any_call("Processed Sensor1 data from 1")
        mock_print.assert_any_call("Processed Sensor2 data from 2")
        mock_print.assert_any_call("Processed Sensor3 data from 3")


if __name__ == '__main__':
    unittest.main()
