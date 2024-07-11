from PythonPractice.EC.src.data_processor.strategy.strategy_interface import IDataProcessingStrategy


class AverageProcessingStrategy(IDataProcessingStrategy):
    def process_data(self, data, **kwargs):
        if not data:
            return None

        try:
            return sum(data) / len(data)
        except Exception as e:
            return None
