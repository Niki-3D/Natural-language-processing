from src.logic.levenshtein import Levenshtein
class ClusterGroup:
    def __init__(self, name_value_dict):
        self.name_value_dict = name_value_dict
        self.clusters = {}
        self.is_similar = Levenshtein.is_similar


    def create_clusters(self):
        # Step 1: Group by first letter of the first string
        first_letter_clusters = {}
        for name in self.name_value_dict:
            first_letter = name.split()[0][0]
            if first_letter not in first_letter_clusters:
                first_letter_clusters[first_letter] = {}
            first_letter_clusters[first_letter][name] = self.name_value_dict[name]
        
        # Step 2: Sub-cluster by first letter of the second string
        for first_letter, names_dict in first_letter_clusters.items():
            self.clusters[first_letter] = {}
            for name, value in names_dict.items():
                second_letter = name.split()[1][0]
                if second_letter not in self.clusters[first_letter]:
                    self.clusters[first_letter][second_letter] = {}
                self.clusters[first_letter][second_letter][name] = value

    def merge_similar_names(self):
        # Step 3: Merge similar names within sub-clusters
        for first_letter, sub_clusters in self.clusters.items():
            for second_letter, names_dict in sub_clusters.items():
                merged_names = {}
                for name in list(names_dict.keys()):
                    if name not in names_dict:
                        continue  # This name has been merged into another, skip it
                    value = names_dict[name]
                    similar_names = [name]
                    
                    for other_name in list(names_dict.keys()):
                        if other_name == name:
                            continue
                        if self.is_similar(name, other_name):
                            similar_names.append(other_name)
                    
                    # Determine the name to keep (with the highest value)
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
                        del names_dict[similar_name]
                    
                    merged_names[best_name] = total_value
                
                self.clusters[first_letter][second_letter] = merged_names

    def get_merged_name_value_dict(self):
        merged_dict = {}
        for first_letter, sub_clusters in self.clusters.items():
            for second_letter, names_dict in sub_clusters.items():
                for name, value in names_dict.items():
                    merged_dict[name] = value
        return merged_dict

# Example usage
name_value_dict = {
    'adam nowak': 101, 'ann nowak': 100, 
    'anna kowalska': 101, 'anna kowalski': 100, 'anna nowak': 101, 
    'jan nowak': 101, 'janina kowalska': 101, 'janina nowak': 105
}

cluster_group = ClusterGroup(name_value_dict)
cluster_group.create_clusters()
cluster_group.merge_similar_names()
merged_name_value_dict = cluster_group.get_merged_name_value_dict()

print(merged_name_value_dict)
