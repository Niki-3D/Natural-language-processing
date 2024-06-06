from src.logic.levenshtein import Levenshtein

class ClusterGroup:
    def __init__(self, name_value_dict):
        """
        Initialize the ClusterGroup with a dictionary of name-value pairs.
        
        Args:
            name_value_dict (dict): Dictionary with names as keys and associated values as values.
        
        Attributes:
            clusters (dict): Dictionary to hold the clustered names.
            is_similar (function): Function to determine if two names are similar based on Levenshtein distance.
        """
        self.name_value_dict = name_value_dict
        self.clusters = {}
        self.is_similar = Levenshtein.is_similar

    def create_clusters(self):
        """
        Create initial clusters based on the first letter of the first and second words in the names.
        
        This method first groups names by the first letter of the first word.
        Then, within each of these groups, it sub-clusters names by the first letter of the second word.
        """
        # Step 1: Group by first letter of the first string (word)
        first_letter_clusters = {}
        for name in self.name_value_dict:
            # Extract the first letter of the first word
            first_letter = name.split()[0][0]
            if first_letter not in first_letter_clusters:
                first_letter_clusters[first_letter] = {}
            # Add the name to the corresponding cluster
            first_letter_clusters[first_letter][name] = self.name_value_dict[name]
        
        # Step 2: Sub-cluster by first letter of the second string (word)
        for first_letter, names_dict in first_letter_clusters.items():
            self.clusters[first_letter] = {}
            for name, value in names_dict.items():
                # Extract the first letter of the second word
                second_letter = name.split()[1][0]
                if second_letter not in self.clusters[first_letter]:
                    self.clusters[first_letter][second_letter] = {}
                # Add the name to the corresponding sub-cluster
                self.clusters[first_letter][second_letter][name] = value

    def merge_similar_names(self):
        """
        Merge similar names within the sub-clusters based on Levenshtein similarity.
        
        This method identifies similar names within each sub-cluster and merges them,
        keeping the name with the highest value and summing the values of the merged names.
        """
        # Step 3: Merge similar names within sub-clusters
        for first_letter, sub_clusters in self.clusters.items():
            for second_letter, names_dict in sub_clusters.items():
                merged_names = {}
                for name in list(names_dict.keys()):
                    if name not in names_dict:
                        continue  # Skip if this name has been merged into another
                    value = names_dict[name]
                    similar_names = [name]
                    
                    # Find all similar names within the same sub-cluster
                    for other_name in list(names_dict.keys()):
                        if other_name == name:
                            continue
                        if self.is_similar(name, other_name):
                            similar_names.append(other_name)
                    
                    # Determine the best name to keep (with the highest value)
                    best_name = name
                    best_value = value
                    total_value = value
                    for similar_name in similar_names:
                        if similar_name == name:
                            continue
                        total_value += names_dict[similar_name]
                        if names_dict[similar_name] > best_value:
                            best_name = similar_name
                            best_value = names_dict[similar_name]
                        # Remove the merged name from the sub-cluster
                        del names_dict[similar_name]
                    
                    # Add the best name with the total value to the merged names dictionary
                    merged_names[best_name] = total_value
                
                # Replace the original sub-cluster with the merged names
                self.clusters[first_letter][second_letter] = merged_names

    def get_merged_name_value_dict(self):
        """
        Flatten the clusters dictionary into a single merged dictionary of name-value pairs.
        
        Returns:
            dict: Merged dictionary with names as keys and their summed values as values.
        """
        merged_dict = {}
        for first_letter, sub_clusters in self.clusters.items():
            for second_letter, names_dict in sub_clusters.items():
                for name, value in names_dict.items():
                    # Add the name and its value to the merged dictionary
                    merged_dict[name] = value
        return merged_dict

    def cluster_names(self):
        """
        Perform the full clustering process and return the merged name-value dictionary.
        
        This method orchestrates the creation of initial clusters, merges similar names,
        and returns the final merged dictionary.
        
        Returns:
            dict: Merged dictionary with names as keys and their summed values as values.
        """
        self.create_clusters()
        self.merge_similar_names()
        return self.get_merged_name_value_dict()
