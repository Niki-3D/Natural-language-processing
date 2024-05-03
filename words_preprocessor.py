import re


class Words_Preprocessor:
    def __init__(self, dict_of_names):
        self.dict_of_names = dict_of_names
        self.cleaned_names = self.clean_names()
        self.names_without_prepositions = self.remove_prepositions()
        self.processed_names = self.process_names()


    def clean_names(self):
        cleaned_names = {}
        for name in self.dict_of_names.keys():
            cleaned_name = re.sub(r'[^a-zA-Z\s]', '', name)
            cleaned_name = re.sub(r'\s+', ' ', cleaned_name)
            cleaned_name = cleaned_name.strip()
            cleaned_names[cleaned_name] = self.dict_of_names[name]
        print(cleaned_names)
        return cleaned_names

    def remove_prepositions(self):
        prepositions = ['for', 'dla']
        modified_names = {}
        for name in self.cleaned_names.keys():
            words = name.split()
            for word in words:
                if word.lower() in prepositions:
                    #modify here
            modified_names[' '.join(words)] = self.cleaned_names[name]
        print(modified_names)
        return modified_names

    def process_names(self):
        processed_names = {}
        for name in self.names_without_prepositions.keys():
            processed_name = name.lower()
            processed_names[processed_name] = self.names_without_prepositions[name]
        print(processed_names)
        return processed_names

    def get_processed_names(self):
        return self.processed_names



dict_of_names = {
    'dla Joe Doe': 1, 'joedoe': 2, 'joe doe': 3, 'joo doee': 4, 'joe DOE': 5, 'Joee Do': 6, '-Joe Doe': 7,
    'John Smith': 5, 'Jon Smiith': 8, 'jooon Smth': 3, 'John Smtih': 2, 'Jonh Smit': 4, 'Jhon Smith': 9,
    'john smit': 7, 'John Smeth': 7, 'Johh Smth': 1, 'jon smtth': 1, 'johnsmith': 1, 'Emily Johnson': 6,
    'Emili Johnsoon': 4, 'Emile Jonsn': 8, 'Emily Johanson': 8, 'Emilly Jhonsen': 10, 'Emlie Johson': 5,
    'emily jhonson': 3, 'emily jhonsn': 5, 'Emly Johsson': 7, 'emily Johnsonn': 9, 'Emiley Johnsson': 10
}

name_processor = Words_Preprocessor(dict_of_names)


print(name_processor.get_processed_names())



