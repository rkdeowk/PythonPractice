from PythonPractice.EC.src.data_processor.strategy.strategy_interface import IDataProcessingStrategy


class DataProcessor:
    def __init__(self):
        self._strategy: IDataProcessingStrategy = None

    def set_strategy(self, strategy: IDataProcessingStrategy):
        self._strategy = strategy

    def get_strategy(self) -> IDataProcessingStrategy:
        return self._strategy

    def process(self, data, **kwargs):
        return self._strategy.process_data(data, **kwargs)
