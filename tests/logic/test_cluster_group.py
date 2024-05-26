import unittest
from src.logic.cluster_group import ClusterGroup

class TestClusterGroup(unittest.TestCase):

    def test_cluster_names(self):
        names = [
            'Jan Kowalski', 'Anna Nowak', 'Janina Kowalska', 
            'Adam Nowak', 'Jan Kowal', 'Ania Nowak', 'Adem Nowak', 'Kowalski Jan'
        ]
        clusters = ClusterGroup.cluster_names(names, initial_threshold=6, nested_threshold=5)
        
        # Print clusters for debugging
        for cluster_label, cluster_names in clusters.items():
            print(f"Cluster {cluster_label}: {cluster_names}")
        
        self.assertEqual(len(clusters), 4)
        self.assertIn(['Jan Kowalski', 'Jan Kowal', 'Kowalski Jan'], clusters.values())
        self.assertIn(['Anna Nowak', 'Ania Nowak'], clusters.values())
        self.assertIn(['Janina Kowalska'], clusters.values())
        self.assertIn(['Adam Nowak', 'Adem Nowak'], clusters.values())

if __name__ == '__main__':
    unittest.main()
