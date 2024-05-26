from src.logic.preprocessor import DataPreprocessor
from src.logic.cluster_group import ClusterGroup

def main():
    # Step 1: Read and preprocess the data
    preprocessor = DataPreprocessor()
    raw_data = preprocessor.read_csv('data/input.csv')
    cleaned_data = preprocessor.clean_data(raw_data)
    
    # Step 2: Extract names and amounts from the cleaned data
    names = [name for name, _ in cleaned_data]
    amounts = {name: amount for name, amount in cleaned_data}
    
    # Step 3: Cluster the names using Levenshtein distance
    clusters = ClusterGroup.cluster_names(names, distance_threshold=3)
    
    # Step 4: Summarize the amounts for each cluster
    cluster_sums = {}
    for cluster_label, cluster_names in clusters.items():
        cluster_sum = sum(amounts[name] for name in cluster_names)
        cluster_sums[cluster_label] = (cluster_names, cluster_sum)
    
    # Step 5: Print the results
    for cluster_label, (cluster_names, cluster_sum) in cluster_sums.items():
        print(f"Cluster {cluster_label}:")
        print(f"Names: {', '.join(cluster_names)}")
        print(f"Total Amount: {cluster_sum}\n")

if __name__ == "__main__":
    main()
