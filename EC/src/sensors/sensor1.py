from PythonPractice.EC.src.sensors.sensor import Sensor


class Sensor1(Sensor):
    def __init__(self, id):
        super().__init__(id)
        self.__is_connected = False

    def connect(self):
        self.__is_connected = True

    def disconnect(self):
        self.__is_connected = False

    def is_connected(self):
        return self.__is_connected

    def read_data(self):
        if not self.__is_connected:
            raise ConnectionError
        return [1.23, 4.56, 7.89]

    def setting(self, **kwargs):
        self.settings = kwargs
