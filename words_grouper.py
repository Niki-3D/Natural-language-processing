from levenshtein_method import Levenshtein_Method
class Names_Grouper:
    #In this class we want to iter through the dictionaryu of names and group then and their values togheter, we will take first name and compare it to all other names, if the similarity is greater than 0.8 we will group them togheter aswell as their values and move them to grouped names dict where their values will add up, then we will do the process as many times as all names are moved or there are only single names in the list in that case we will move them all by themselves
    def __init__(self, dict_of_names):
        self.dict_of_names = dict_of_names
        self.grouped_names = self.group_names()

    def group_names(self):
        levenshtein_method = Levenshtein_Method()
        grouped_names = {}
        names = list(self.dict_of_names.keys())
        while names:
            name = names.pop(0)
            grouped_names[name] = self.dict_of_names[name]
            for n in names:
                if levenshtein_method.is_similar(name, n, 0.8):
                    grouped_names[name] += self.dict_of_names[n]
                    names.remove(n)
        return grouped_names

    def get_grouped_names(self):
        return self.grouped_names


dict_of_names = {'Joe Doe': 5, 'joedoe': 4, '-Joe Doe': 2, 'joe doe': 3, 'joo doee': 9, 'joe DOE': 10, 'Joee Do': 5,
                 'John Smith': 5, 'Jon Smiith': 8, 'jooon Smth': 3, 'John Smtih': 2, 'Jonh Smit': 4, 'Jhon Smith': 9,
                 'john smit': 7, 'John Smeth': 7, 'Johh Smth': 1, 'jon smtth': 1, 'johnsmith': 1, 'Emily Johnson': 6,
                 'Emili Johnsoon': 4, 'Emile Jonsn': 8, 'Emily Johanson': 8, 'Emilly Jhonsen': 10, 'Emlie Johson': 5,
                 'emily jhonson': 3, 'emily jhonsn': 5, 'Emly Johsson': 7, 'emily Johnsonn': 9, 'Emiley Johnsson': 10}
