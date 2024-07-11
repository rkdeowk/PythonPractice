from src.data_processor.strategy.strategy_interface import IDataProcessingStrategy


class MaxProcessingStrategy(IDataProcessingStrategy):
    def process_data(self, data, **kwargs):
        return max(data) if data else None