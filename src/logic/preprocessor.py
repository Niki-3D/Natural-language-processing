import csv
import re

class DataPreprocessor:

    def __init__(self):
        self.prepositions = ['dla', 'do', 'na', 'w', 'o', 'u', 'z', 'za', 'bez', 'przez', 'po', 'pod']

    def read_csv(self, file_path):
        data = []
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=';')
            for row in reader:
                name = row[0].strip()
                amount = float(row[1].strip())
                data.append((name, amount))
        return data

    def normalize_string(self, string):
        string = string.lower()
        string = re.sub(r'\W+', ' ', string)
        return string.strip()

    def remove_prepositions(self, string):
        string = self.normalize_string(string)
        words = string.split()
        original_words = words.copy()  
        filtered_words = [word for word in words if word not in self.prepositions]
        return ' '.join(filtered_words)

    def clean_data(self, raw_data):
        cleaned_data = []
        for name, amount in raw_data:
            name = self.remove_prepositions(name)
            cleaned_data.append((name, amount))
        return cleaned_data

    def to_dict(self, cleaned_data):
        data_dict = {}
        for name, amount in cleaned_data:
            if name in data_dict:
                data_dict[name] += amount
            else:
                data_dict[name] = amount

        # Round the values to two decimal places
        data_dict = {k: round(v, 2) for k, v in data_dict.items()}
        return data_dict
    
    def alphabetically_sort_and_sum_up_strings(self, data_dict):
        sorted_dict = {}
        for key in data_dict.keys():
            names = key.split()
            names.sort()
            sorted_key = ' '.join(names)
            if sorted_key in sorted_dict:
                sorted_dict[sorted_key] += data_dict[key]
            else:
                sorted_dict[sorted_key] = data_dict[key]
        
        return sorted_dict
    
    def alphabetically_sort_dicts(self, data_dict):
        return {key: data_dict[key] for key in sorted(data_dict.keys())}
            

    def process(self, file_path):
        data = self.read_csv(file_path)
        cleaned_data = self.clean_data(data)
        data_dict = self.to_dict(cleaned_data)
        sorted_values = self.alphabetically_sort_and_sum_up_strings(data_dict)
        return self.alphabetically_sort_dicts(sorted_values)

   


