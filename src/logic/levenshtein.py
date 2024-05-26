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
    def are_similar(string1, string2, threshold=2):
        """
        Determine if two strings are similar within a given Levenshtein distance threshold.
        
        Args:
            string1 (str): The first string.
            string2 (str): The second string.
            threshold (int, optional): The Levenshtein distance threshold for similarity. Defaults to 2.
        
        Returns:
            bool: True if the strings are similar, False otherwise.
        """
        return Levenshtein.calculate_distance(string1, string2) <= threshold
