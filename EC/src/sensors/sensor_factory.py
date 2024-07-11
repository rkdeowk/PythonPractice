from enum import Enum

from src.sensors.sensor1 import Sensor1
from src.sensors.sensor2 import Sensor2
from src.sensors.sensor3 import Sensor3


class SensorType(str, Enum):
    SENSOR1 = 'sensor1',
    SENSOR2 = 'sensor2',
    SENSOR3 = 'sensor3'


class SensorFactory:
    @staticmethod
    def create_sensor(sensor_type: str, sensor_id: str):
        if sensor_type.lower() == SensorType.SENSOR1:
            return Sensor1(sensor_id)
        elif sensor_type.lower() == SensorType.SENSOR2:
            return Sensor2(sensor_id)
        elif sensor_type.lower() == SensorType.SENSOR3:
            return Sensor3(sensor_id)
        else:
            raise ValueError(f'Unknown sensor type: {sensor_type}')
