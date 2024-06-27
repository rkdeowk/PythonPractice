import unittest

from PythonPractice.EC.src.data_processor.data_processor import DataProcessor


class TestDataProcessor(unittest.TestCase):
    def test_process(self):
        processor = DataProcessor()
        self.assertEqual(processor.process("test data"), "Processed test data")


if __name__ == '__main__':
    unittest.main()
