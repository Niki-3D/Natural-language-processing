import unittest
from src.logic.levenshtein import Levenshtein
from src.logic.cluster_group import ClusterGroup

class TestClusterGroup(unittest.TestCase):

    def test_cluster_names(self):
        name_value_dict = {
            'adam nowak': 101, 'ann nowak': 100,
            'anna kowalska': 101, 'anna kowalski': 100, 'anna nowak': 101,
            'jan nowak': 101, 'janina kowalska': 101, 'janina nowak': 105
        }
        
        expected_output = {
            'adam nowak': 101, 'anna nowak': 201, 'anna kowalska': 201,
            'jan nowak': 101, 'janina nowak': 105, 'janina kowalska': 101
        }
        
        cluster_group = ClusterGroup(name_value_dict)
        result = cluster_group.cluster_names()
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()
