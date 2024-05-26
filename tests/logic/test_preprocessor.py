import unittest
from src.logic.preprocessor import DataPreprocessor

class TestDataPreprocessor(unittest.TestCase):

    def setUp(self):
        self.preprocessor = DataPreprocessor()

    def test_read_csv(self):
        data = self.preprocessor.read_csv('tests/data/input.csv')
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)

    def test_normalize_string(self):
        result = self.preprocessor.normalize_string('Jan Kowalski!')
        self.assertEqual(result, 'jan kowalski')

    def test_remove_prepositions(self):
        result = self.preprocessor.remove_prepositions('dla Jana Kowalskiego')
        self.assertEqual(result, 'jana kowalskiego')

    def test_clean_data(self):
        raw_data = [
            ('Jan Kowalski', 12.50),
            ('dla Jana Kowalskiego', 33.70)
        ]
        cleaned_data = self.preprocessor.clean_data(raw_data)
        expected_data = [
            ('jan kowalski', 12.50),
            ('jana kowalskiego', 33.70)
        ]
        self.assertEqual(cleaned_data, expected_data)

if __name__ == '__main__':
    unittest.main()
