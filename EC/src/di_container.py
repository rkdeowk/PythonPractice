class DIContainer:
    def __init__(self):
        self._services = {}

    def register(self, name, instance):
        self._services[name] = instance

    def resolve(self, name):
        return self._services.get(name)
