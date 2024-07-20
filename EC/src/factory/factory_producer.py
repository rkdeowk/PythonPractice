from PythonPractice.EC.src.factory.factory_abstract import AbstractFactory
from PythonPractice.EC.src.factory.factory_sensor1 import Sensor1Factory
from PythonPractice.EC.src.factory.factory_sensor2 import Sensor2Factory
from PythonPractice.EC.src.logger.logger import Logger
from PythonPractice.EC.src.sensors.sensor_type import SensorType


class FactoryProducer:
    _factories: dict[SensorType, AbstractFactory] = {
        SensorType.SENSOR1: Sensor1Factory(),
        SensorType.SENSOR2: Sensor2Factory(),
    }

    def __init__(self):
        self.logger = Logger(self.__class__.__name__).get_logger()
        self.logger.info(f'create {self.__class__.__name__}')

    def get_factory(self, sensor_type: SensorType) -> AbstractFactory:
        factory = self._factories.get(sensor_type)
        if factory is None:
            self.logger.info(f'Unknown sensor type: {sensor_type}')
            raise ValueError(f'Unknown sensor type: {sensor_type}')
        return factory

    def set_factory(self, sensor_type: SensorType, factory: AbstractFactory):
        self.logger.info(f'set factory: {factory.__class__.__name__}')
        self._factories[sensor_type] = factory
