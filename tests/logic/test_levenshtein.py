import unittest
from src.logic.levenshtein import Levenshtein

class TestLevenshtein(unittest.TestCase):

    def test_calculate_distance_basic(self):
        self.assertEqual(Levenshtein.calculate_distance('kitten', 'sitting'), 3)

    def test_calculate_distance_with_substitutions(self):
        self.assertEqual(Levenshtein.calculate_distance('flaw', 'lawn'), 2)

    def test_calculate_distance_with_empty_string1(self):
        self.assertEqual(Levenshtein.calculate_distance('', 'test'), 4)

    def test_calculate_distance_with_empty_string2(self):
        self.assertEqual(Levenshtein.calculate_distance('test', ''), 4)

    def test_are_similar_returns_true_for_similar_names(self):
        self.assertTrue(Levenshtein.are_similar('Jan Kowalski', 'Jan Kowal'))

    def test_are_similar_returns_true_for_reversed_names(self):
        self.assertTrue(Levenshtein.are_similar('Jan Kowalski', 'Kowalski Jan'))

    def test_are_similar_returns_true_for_variation_of_name(self):
        self.assertTrue(Levenshtein.are_similar('Ania Nowak', 'Nowak Anna'))

    def test_are_similar_returns_false_for_different_names(self):
        self.assertFalse(Levenshtein.are_similar('Jan Kowalski', 'Janina Kowalska'))

    def test_are_similar_returns_true_for_variation_of_surname(self):
        self.assertTrue(Levenshtein.are_similar('Adam Nowak', 'Nowak Adem'))

    def test_are_similar_returns_false_for_completely_different_names(self):
        self.assertFalse(Levenshtein.are_similar('John Smith', 'Jane Doe'))

if __name__ == '__main__':
    unittest.main()
