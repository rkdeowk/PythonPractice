from PythonPractice.EC.src.data_processor.strategy.strategy_interface import IDataProcessingStrategy


class FindPeakProcessingStrategy(IDataProcessingStrategy):
    def __init__(self, threshold=None):
        self.threshold = threshold

    def process_data(self, data, **kwargs):
        if not data:
            return [], []

        peak, peak_indices = [], []
        try:
            for i in range(1, len(data) - 1):
                if data[i] >= self.threshold and data[i] > data[i - 1] and data[i] > data[i + 1]:
                    peak.append(data[i])
                    peak_indices.append(i)
            return peak, peak_indices
        except Exception as e:
            return [], []
