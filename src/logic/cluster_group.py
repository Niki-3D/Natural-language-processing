import numpy as np
from sklearn.cluster import AgglomerativeClustering
from src.logic.levenshtein import Levenshtein

class ClusterGroup:
    
    @staticmethod
    def cluster_names(names, initial_threshold=6, nested_threshold=5):
        # Step 1: Initial Clustering
        initial_distances = np.zeros((len(names), len(names)))
        for i in range(len(names)):
            for j in range(len(names)):
                if i != j:
                    initial_distances[i, j] = Levenshtein.calculate_distance(names[i], names[j])

        initial_clustering = AgglomerativeClustering(
            n_clusters=None,
            metric='precomputed',
            linkage='complete',
            distance_threshold=initial_threshold
        )
        initial_clustering.fit(initial_distances)
        
        # Group names by initial clusters
        initial_clusters = {}
        for name, label in zip(names, initial_clustering.labels_):
            if label not in initial_clusters:
                initial_clusters[label] = []
            initial_clusters[label].append(name)
        
        # Step 2: Nested Clustering within initial clusters
        final_clusters = {}
        cluster_counter = 0
        for cluster_label, cluster_names in initial_clusters.items():
            if len(cluster_names) == 1:
                final_clusters[cluster_counter] = cluster_names
                cluster_counter += 1
                continue
            
            nested_distances = np.zeros((len(cluster_names), len(cluster_names)))
            for i in range(len(cluster_names)):
                for j in range(len(cluster_names)):
                    if i != j:
                        nested_distances[i, j] = Levenshtein.calculate_distance(cluster_names[i], cluster_names[j])
            
            nested_clustering = AgglomerativeClustering(
                n_clusters=None,
                metric='precomputed',
                linkage='complete',
                distance_threshold=nested_threshold
            )
            nested_clustering.fit(nested_distances)
            
            for nested_name, nested_label in zip(cluster_names, nested_clustering.labels_):
                if cluster_counter not in final_clusters:
                    final_clusters[cluster_counter] = []
                final_clusters[cluster_counter].append(nested_name)
            cluster_counter += 1
        
        # Step 3: Fine-tune Clustering using are_similar method
        refined_clusters = {}
        for cluster_label, cluster_names in final_clusters.items():
            refined_clusters[cluster_label] = ClusterGroup.refine_clusters(cluster_names)
        
        return refined_clusters

    @staticmethod
    def refine_clusters(names):
        clusters = {}
        for name in names:
            matched = False
            for cluster_key, cluster_names in clusters.items():
                if any(Levenshtein.are_similar(name, existing_name) for existing_name in cluster_names):
                    clusters[cluster_key].append(name)
                    matched = True
                    break
            if not matched:
                clusters[len(clusters)] = [name]
        
        return clusters
