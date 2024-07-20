from PythonPractice.EC.src.data_processor.strategy.strategy_interface import IDataProcessingStrategy
from PythonPractice.EC.src.logger.logger import Logger


class DataProcessor:
    def __init__(self):
        self._strategy: IDataProcessingStrategy = None
        self.logger = Logger(self.__class__.__name__).get_logger()
        self.logger.info(f'create {self.__class__.__name__}')

    def set_strategy(self, strategy: IDataProcessingStrategy):
        self._strategy = strategy
        self.logger.info(f'set strategy {strategy.__class__.__name__}')

    def get_strategy(self) -> IDataProcessingStrategy:
        self.logger.info(f'get strategy {self._strategy.__class__.__name__}')
        return self._strategy

    def process(self, data, **kwargs):
        result = self._strategy.process_data(data, **kwargs)
        self.logger.info(f'process: {data}, result: {result}')
        return result
