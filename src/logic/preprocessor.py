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
        # Normalize the string first
        string = self.normalize_string(string)
        words = string.split()
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
        return data_dict

if __name__ == "__main__":
    preprocessor = DataPreprocessor()
    data = preprocessor.read_csv('src/data/input.csv')
    cleaned_data = preprocessor.clean_data(data)
    data_dict = preprocessor.to_dict(cleaned_data)
    print(data_dict)
