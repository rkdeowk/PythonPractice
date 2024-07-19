import unittest

from src.factory.factory_producer import FactoryProducer
from src.sensors.sensor_type import SensorType


class TestParser(unittest.TestCase):
    def setUp(self):
        self.data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        factory_producer = FactoryProducer()
        self.sensor1_parser = factory_producer.get_factory(SensorType.SENSOR1).create_parser()
        self.sensor2_parser = factory_producer.get_factory(SensorType.SENSOR2).create_parser()

    def test_sensor1_parser(self):
        parsed_data = self.sensor1_parser.parse(self.data)
        self.assertEqual(parsed_data, self.data)

        parsed_data = self.sensor1_parser.parse_other_data(self.data)
        self.assertEqual(parsed_data, self.data)

    def test_sensor2_parser(self):
        parsed_data = self.sensor2_parser.parse(self.data)
        self.assertEqual(parsed_data, self.data)

        parsed_data = self.sensor2_parser.parse_other_data(self.data)
        self.assertEqual(parsed_data, self.data)


if __name__ == '__main__':
    unittest.main()
