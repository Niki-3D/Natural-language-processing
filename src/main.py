from src.logic.preprocessor import DataPreprocessor
from src.logic.cluster_group import ClusterGroup

def main():
    preprocessor = DataPreprocessor()
    data = preprocessor.process('src/data/input.csv')
    cluster_group = ClusterGroup(data)
    cluster_group.create_clusters()
    cluster_group.merge_similar_names()
    print(cluster_group.clusters)

if __name__ == '__main__':
    main()