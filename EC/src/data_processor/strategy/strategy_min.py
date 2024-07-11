from PythonPractice.EC.src.data_processor.strategy.strategy_interface import IDataProcessingStrategy


class MinProcessingStrategy(IDataProcessingStrategy):
    def process_data(self, data, **kwargs):
        return min(data) if data else None
