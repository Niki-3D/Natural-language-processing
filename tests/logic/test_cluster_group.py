import unittest

class TestClusterGroup(unittest.TestCase):

    def test_cluster_names(self):
        names = {'jan kowalski': 12.5, 'anna nowak': 23.0, 'jana kowalskiego': 133.6, 
                 'nowak anna': 133.0, 'janina kowalska': 45.2, 'nowak adam': 155.4, 
                 'anny nowak': 89.5, 'kowalski jan': 101.2, 'kowalska janina': 112.3, 
                 'adam nowak': 56.4, 'jana nowaka': 78.9, 'nowak jan': 90.5, 
                 'kowalski anna': 67.8, 'adama kowalskiego': 123.4, 'nowak janina': 78.9, 
                 'kowalska anna': 56.7, 'jan kowlaski': 55.3}
        

if __name__ == '__main__':
    unittest.main()
