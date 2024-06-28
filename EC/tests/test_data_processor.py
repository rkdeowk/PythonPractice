import unittest
from unittest.mock import Mock
from PythonPractice.EC.src.data_processor.data_processor import DataProcessor


class TestDataProcessor(unittest.TestCase):
    def test_process(self):
        processor = Mock(Spec=DataProcessor)
        processor.process.side_effect = lambda data: sum(data)
        result = processor.process([1.23, 4.56, 7.89])
        self.assertEqual(result, 13.68)
        processor.process.assert_called_once_with([1.23, 4.56, 7.89])


if __name__ == '__main__':
    unittest.main()
