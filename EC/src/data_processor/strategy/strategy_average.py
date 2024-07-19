from src.data_processor.strategy.strategy_interface import IDataProcessingStrategy


class AverageProcessingStrategy(IDataProcessingStrategy):
    def process_data(self, data, **kwargs):
        if len(data) == 0:
            return None

        return sum(data) / len(data)
