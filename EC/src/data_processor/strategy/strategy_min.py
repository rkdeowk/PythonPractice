from PythonPractice.EC.src.data_processor.strategy.strategy_interface import IDataProcessingStrategy


class MinProcessingStrategy(IDataProcessingStrategy):
    def process_data(self, data, **kwargs):
        if not data:
            return None

        try:
            return min(data)
        except Exception as e:
            return None
