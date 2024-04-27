import re
from collections import defaultdict

class NameAnalyzis:
    def __init__(self, list_of_names):
        self.list_of_names = list_of_names
        self.clean_names = [self.clean_name(name) for name in self.list_of_names]
        self.processed_names = [self.remove_unnecessary_characters(name) for name in self.clean_names]
        self.name_counts = self.count_names()

    def clean_name(self, name):
        return name.strip().title()

    def remove_unnecessary_characters(self, name):
        return re.sub(r"[^\w\s]", "", name).replace("  ", " ")

    def count_names(self):
        name_counts = defaultdict(int)
        for name in self.processed_names:
            name_counts[name] += 1
        return name_counts

    def get_name_counts(self):
        return dict(self.name_counts)


list_of_names = [
    "Joe Doe", "joedoe", "-Joe Doe", "joe doe", "joo doee", "   joe DOE  ", "Joe Doe", "joe doe", "Joee Do",
    "John Smith", "Jon Smiith", "jooon Smth", "John Smtih", "Jonh Smit", "Jhon Smith", "john smit", "   John Smeth", "John Smith", "Johh Smth", "jon smtth", "johnsmith",
    "Emily Johnson", "Emili Johnsoon", "Emile Jonsn", "Emily Johanson", "Emilly Jhonsen", "Emlie Johson", "  emily jhonson  ", "emily jhonsn", "Emily Johnson", "Emly Johsson", "emily Johnsonn", "Emiley Johnsson"
]

name_processor = NameAnalyzis(list_of_names)
name_counts = name_processor.get_name_counts()

for name, count in name_counts.items():
    print(f"{name}: {count}")
