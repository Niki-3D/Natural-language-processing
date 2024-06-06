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
            string1, string2 = string2, string1

        if len(string2) == 0:
            return len(string1)

        previous_row = list(range(len(string2) + 1))
        current_row = [0] * (len(string2) + 1)

        for i, char1 in enumerate(string1):
            current_row[0] = i + 1
            for j, char2 in enumerate(string2):
                insertions = previous_row[j + 1] + 1
                deletions = current_row[j] + 1
                substitutions = previous_row[j] + (char1 != char2)
                current_row[j + 1] = min(insertions, deletions, substitutions)
            previous_row, current_row = current_row, previous_row

        return previous_row[-1]
    

    @staticmethod
    def is_similar(string1, string2, surname_threshold=3, name_threshold=2):
        """
        Determine if two names are similar based on Levenshtein distance thresholds.

        Args:
            string1 (str): The first name.
            string2 (str): The second name.
            surname_threshold (int): Threshold for surname similarity.
            name_threshold (int): Threshold for first name similarity.

        Returns:
            bool: True if both surnames and first names are within their respective thresholds, False otherwise.
        """
        first1, last1 = split_name(string1)
        first2, last2 = split_name(string2)

        surname_distance = Levenshtein.calculate_distance(last1, last2)
        name_distance = Levenshtein.calculate_distance(first1, first2)

        return surname_distance <= surname_threshold and name_distance <= name_threshold
