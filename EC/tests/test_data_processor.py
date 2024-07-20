import unittest

from PythonPractice.EC.src.data_processor.data_processor import DataProcessor
from PythonPractice.EC.src.data_processor.strategy.strategy_average import AverageProcessingStrategy
from PythonPractice.EC.src.data_processor.strategy.strategy_find_peak import FindPeakProcessingStrategy

DATA = [10, 20, 30, 40, 30, 20, 10]


class TestDataProcessor(unittest.TestCase):
    def test_set_strategy(self):
        strategy = AverageProcessingStrategy()
        data_processor = DataProcessor()
        data_processor.set_strategy(strategy)
        self.assertEqual(data_processor.get_strategy(), strategy)

    def test_average_strategy(self):
        data_processor = DataProcessor()
        data_processor.set_strategy(AverageProcessingStrategy())
        result = data_processor.process(DATA)
        self.assertEqual(result, sum(DATA) / len(DATA))

    def test_find_peak_strategy(self):
        data_processor = DataProcessor()
        data_processor.set_strategy(FindPeakProcessingStrategy(threshold=10))
        peak, peak_indices = data_processor.process(DATA)
        self.assertEqual(peak, [40])
        self.assertEqual(peak_indices, [3])

    def test_find_peak_fail_strategy(self):
        data_processor = DataProcessor()
        data_processor.set_strategy(FindPeakProcessingStrategy(threshold=50))
        peak, peak_indices = data_processor.process(DATA)
        self.assertEqual(peak, [])
        self.assertEqual(peak_indices, [])


if __name__ == '__main__':
    unittest.main()
