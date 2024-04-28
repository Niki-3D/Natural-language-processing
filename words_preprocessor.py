import re
from collections import defaultdict

class Words_Preprocessor:
    def __init__(self, dict_of_names):
        self.dict_of_names = dict_of_names
        self.cleaned_names = self.clean_names()
        self.processed_names = self.process_names()
        self.name_counts = self.count_names_greater_than_one()

    def clean_names(self):
        cleaned_names = []
        for name in self.dict_of_names.keys():
            cleaned_name = re.sub(r'[^a-zA-Z\s]', '', name)
            cleaned_name = re.sub(r'\s+', ' ', cleaned_name)
            cleaned_name = cleaned_name.strip()
            cleaned_names.append(cleaned_name)
        return cleaned_names

    def process_names(self):
        processed_names = []
        for name in self.cleaned_names:
            processed_name = name.lower()
            processed_names.append(processed_name)
        return processed_names

    def count_names_greater_than_one(self):
        name_counts = defaultdict(int)
        for name in self.processed_names:
            name_counts[name] += 1
        return {name: count for name, count in name_counts.items() if count > 1}

    def get_processed_names(self):
        return self.processed_names

    def get_name_counts(self):
        return self.name_counts


dict_of_names = {
    'Joe Doe': 5, 'joedoe': 4, '-Joe Doe': 2, 'joe doe': 3, 'joo doee': 9, 'joe DOE': 10, 'Joee Do': 5,
    'John Smith': 5, 'Jon Smiith': 8, 'jooon Smth': 3, 'John Smtih': 2, 'Jonh Smit': 4, 'Jhon Smith': 9,
    'john smit': 7, 'John Smeth': 7, 'Johh Smth': 1, 'jon smtth': 1, 'johnsmith': 1, 'Emily Johnson': 6,
    'Emili Johnsoon': 4, 'Emile Jonsn': 8, 'Emily Johanson': 8, 'Emilly Jhonsen': 10, 'Emlie Johson': 5,
    'emily jhonson': 3, 'emily jhonsn': 5, 'Emly Johsson': 7, 'emily Johnsonn': 9, 'Emiley Johnsson': 10
}

name_processor = Words_Preprocessor(dict_of_names)
name_counts = name_processor.count_names_greater_than_one()

print(name_counts)
print(name_processor.get_processed_names())

