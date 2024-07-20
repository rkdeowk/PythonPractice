from PythonPractice.EC.src.logger.logger import Logger
from PythonPractice.EC.src.sensors.sensor1 import Sensor1
from PythonPractice.EC.src.sensors.sensor2 import Sensor2


def main():
    sensor1 = Sensor1('sensor1')
    sensor2 = Sensor2('sensor2')

    sensor1.connect()
    data = sensor1.get_data()
    sensor1.disconnect()


if __name__ == '__main__':
    main()
