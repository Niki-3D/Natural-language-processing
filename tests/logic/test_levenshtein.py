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

    def test_is_name_similar_returns_any_value(self):
        self.assertIsNotNone(Levenshtein.is_similar('adam kowalskieg', 'adam kowalski'))

    def test_is_name_similar_returns_boolean(self):
        self.assertIsInstance(Levenshtein.is_similar('adam kowalskieg', 'adam kowalski'), bool)

    def test_is_name_similar_returns_true(self):
        self.assertTrue(Levenshtein.is_similar('adam kowalskieg', 'adam kowalski'))

    def test_is_name_similar_returns_true_in_edge_case(self):
        self.assertTrue(Levenshtein.is_similar('ann nowa', 'ania nowak'))

    def test_is_name_similar_returns_false(self):
        self.assertFalse(Levenshtein.is_similar('anna nowa', 'adam nowak'))

    def test_is_name_similar_returns_false_in_edge_case(self):
        self.assertFalse(Levenshtein.is_similar('jan nowak', 'janina nowak'))
        
if __name__ == '__main__':
    unittest.main()

