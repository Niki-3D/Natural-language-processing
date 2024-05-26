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
        
        # Check if similar names are clustered together
        self.assertTrue(any('Jan Kowalski' in cluster and 'Jan Kowal' in cluster for cluster in clusters.values()))
        self.assertTrue(any('Anna Nowak' in cluster and 'Ania Nowak' in cluster for cluster in clusters.values()))
        self.assertTrue(any('Adam Nowak' in cluster and 'Adem Nowak' in cluster for cluster in clusters.values()))
        self.assertTrue(any('Jan Kowalski' in cluster and 'Kowalski Jan' in cluster for cluster in clusters.values()))

if __name__ == '__main__':
    unittest.main()
