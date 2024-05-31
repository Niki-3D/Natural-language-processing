from src.logic.levenshtein import Levenshtein
import numpy as np

class ClusterGroup:
    pass
        
names = {
'jan kowalski': 10, 'anna nowak': 10, 'jana kowalskiego': 10,
'nowak anna': 10, 'janina kowalska': 10, 'nowak adam': 10,
'anny nowak': 10, 'kowalski jan': 10, 'kowalska janina': 10,
'adam nowak': 10, 'jana nowaka': 10., 'nowak jan': 10.,
'kowalski anna': 10., 'adama kowalskiego': 10., 'nowak janina': 10.,
'kowalska anna': 10., 'jan kowlaski': 10.
}

cluster_group = ClusterGroup()
clustered_names = cluster_group.cluster_names(names)
print(clustered_names)