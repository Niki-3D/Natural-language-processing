from src.utils.clustering_tools import split_name

class Levenshtein:
    @staticmethod
    def calculate_distance(string1, string2):
        """
        Calculate the Levenshtein distance between two strings.
        
        Args:
            string1 (str): The first string.
            string2 (str): The second string.
        
        Returns:
            int: The Levenshtein distance between the two strings.
        """
        if len(string1) < len(string2):
            return Levenshtein.calculate_distance(string2, string1)

        if len(string2) == 0:
            return len(string1)

        previous_row = range(len(string2) + 1)
        for i, char1 in enumerate(string1):
            current_row = [i + 1]
            for j, char2 in enumerate(string2):
                insertions = previous_row[j + 1] + 1
                deletions = current_row[j] + 1
                substitutions = previous_row[j] + (char1 != char2)
                current_row.append(min(insertions, deletions, substitutions))
            previous_row = current_row

        return previous_row[-1]

    @staticmethod
    def are_similar(string1, string2, surname_threshold=3, name_threshold=2):
        """
        Determine if two names are similar or reversed versions of each other within given Levenshtein distance thresholds.
        
        Args:
            string1 (str): The first name.
            string2 (str): The second name.
            surname_threshold (int, optional): The Levenshtein distance threshold for surname similarity. Defaults to 3.
            name_threshold (int, optional): The Levenshtein distance threshold for name similarity. Defaults to 2.
        
        Returns:
            bool: True if the names are similar or reversed, False otherwise.
        """
        first1, last1 = split_name(string1)
        first2, last2 = split_name(string2)

        if Levenshtein.calculate_distance(last1, last2) <= surname_threshold:
            if Levenshtein.calculate_distance(first1, first2) <= name_threshold:
                return True
        elif Levenshtein.calculate_distance(last1, first2) <= 1:
            if Levenshtein.calculate_distance(first1, last2) <= 1:
                return True

        return False
#ALFABETYCZNIE SORTUJEMY

def alphabetically_sort(data_dict):
    pass

def usun_ostatnia_litere_przy_dla(data_dict):
    pass

def fuzzy_group(data_dict):
    pass


def sortuj_alfabetycznie(data_dict):
    pass