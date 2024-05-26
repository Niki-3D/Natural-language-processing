import unittest
from src.logic.levenshtein import Levenshtein

class TestLevenshtein(unittest.TestCase):

    def test_calculate_distance(self):
        self.assertEqual(Levenshtein.calculate_distance('kitten', 'sitting'), 3)
        self.assertEqual(Levenshtein.calculate_distance('flaw', 'lawn'), 2)


    def test_are_similar(self):
        self.assertTrue(Levenshtein.are_similar('kitten', 'kittens', threshold=2))

    def test_are_not_similar(self):
        self.assertFalse(Levenshtein.are_similar('kitten', 'sitting', threshold=2))


    def test_are_names_similar_returns_true(self):
        self.assertTrue(Levenshtein.are_similar('Jan Kowalski', 'Jan Kowal', threshold=2))
    
    def test_are_names_similar_returns_false(self):
        self.assertFalse(Levenshtein.are_similar('Anna Nowak', 'Adam Nowak', threshold=3))
        


    

if __name__ == '__main__':
    unittest.main()
