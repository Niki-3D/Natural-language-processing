from src.logic.preprocessor import DataPreprocessor
from src.logic.cluster_group import ClusterGroup
from src.logic.processor import Processor

def main():
    preprocessor = DataPreprocessor()
    data = preprocessor.process('src/data/input.csv')
    cluster_group = ClusterGroup(data)
    cluster_group.create_clusters()
    cluster_group.merge_similar_names()
    result = cluster_group.clusters
    processor = Processor(result)
    processor.run_processor(result)


if __name__ == '__main__':
    main()