from PythonPractice.EC.src.factory.factory_abstract import AbstractFactory
from PythonPractice.EC.src.factory.factory_sensor1 import Sensor1Factory
from PythonPractice.EC.src.factory.factory_sensor2 import Sensor2Factory
from PythonPractice.EC.src.sensors.sensor_type import SensorType


class FactoryProducer:
    _factories: dict[SensorType, AbstractFactory] = {
        SensorType.SENSOR1: Sensor1Factory(),
        SensorType.SENSOR2: Sensor2Factory(),
    }

    @classmethod
    def get_factory(cls, sensor_type: SensorType) -> AbstractFactory:
        factory = cls._factories.get(sensor_type)
        if factory is None:
            raise ValueError(f'Unknown sensor type: {sensor_type}')
        return factory

    @classmethod
    def set_factory(cls, sensor_type: SensorType, factory: AbstractFactory):
        cls._factories[sensor_type] = factory
