from PythonPractice.EC.src.controller.sensor_command import ConnectSensorCommand
from PythonPractice.EC.src.controller.sensor_controller import SensorManager, SensorController
from PythonPractice.EC.src.logger.logger import container
from PythonPractice.EC.src.sensors.sensor_factory import SensorType, SensorFactory
from PythonPractice.EC.src.services.sensor_service import SensorService

sensor_service = SensorService(container.resolve('Logger'))
sensor_manager = SensorManager()
sensor_controller = SensorController(sensor_manager)

sensor1 = SensorFactory.create_sensor(SensorType.SENSOR1, '1')
sensor2 = SensorFactory.create_sensor(SensorType.SENSOR2, '2')
sensor3 = SensorFactory.create_sensor(SensorType.SENSOR3, '3')

sensor_service.add_sensor(sensor_manager, sensor1)
sensor_service.add_sensor(sensor_manager, sensor2)
sensor_service.add_sensor(sensor_manager, sensor3)

sensor_service.execute_command(sensor_controller, ConnectSensorCommand(sensor1))
