import unittest

from PythonPractice.EC.src.controller.sensor_command import ConnectSensorCommand, GetDataSensorCommand
from PythonPractice.EC.src.controller.sensor_controller import SensorController
from PythonPractice.EC.src.data_processor.data_processor import DataProcessor
from PythonPractice.EC.src.data_processor.strategy.strategy_average import AverageProcessingStrategy
from PythonPractice.EC.src.factory.factory_producer import FactoryProducer
from PythonPractice.EC.src.sensors.sensor_type import SensorType


class TestAll(unittest.TestCase):
    def test_working_process(self):
        factory_producer = FactoryProducer()
        sensor1 = factory_producer.get_factory(SensorType.SENSOR1).create_sensor('sensor1')
        sensor2 = factory_producer.get_factory(SensorType.SENSOR2).create_sensor('sensor2')
        sensor1_parser = factory_producer.get_factory(SensorType.SENSOR1).create_parser()
        sensor2_parser = factory_producer.get_factory(SensorType.SENSOR2).create_parser()

        sensor_controller = SensorController()
        sensor_controller.add_sensor(sensor1)
        sensor_controller.add_sensor(sensor2)

        data_processor = DataProcessor()
        data_processor.set_strategy(AverageProcessingStrategy())

        for sensor, parser in zip([sensor1, sensor2], [sensor1_parser, sensor2_parser]):
            sensor_controller.execute_command(ConnectSensorCommand(sensor))

            data = sensor_controller.execute_command(GetDataSensorCommand(sensor))
            data_parsed = parser.parse(data)
            data_processed = data_processor.process(data_parsed)

            print(sensor.sensor_id, data, data_parsed, data_processed)


if __name__ == '__main__':
    unittest.main()
