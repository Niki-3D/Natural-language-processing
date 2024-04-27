class Levenshtein_Method:
    # This method is used to calculate the Levenshtein distance between two strings
    def levenshtein_distance(self, string1, string2):
        # Create a matrix of zeros with dimensions (len(string1)+1) x (len(string2)+1)
        matrix = [[0 for n in range(len(string2) + 1)] for m in range(len(string1) + 1)]

        # Initialize the first row and column of the matrix
        for i in range(len(string1) + 1):
            matrix[i][0] = i
        for j in range(len(string2) + 1):
            matrix[0][j] = j

        # Fill in the rest of the matrix
        for i in range(1, len(string1) + 1):
            for j in range(1, len(string2) + 1):
                if string1[i - 1] == string2[j - 1]:
                    substitution_cost = 0
                else:
                    substitution_cost = 1
                matrix[i][j] = min(matrix[i - 1][j] + 1,  # deletion
                                   matrix[i][j - 1] + 1,  # insertion
                                   matrix[i - 1][j - 1] + substitution_cost)

        # Return the bottom-right value of the matrix
        return matrix[-1][-1]

    # This method is used to calculate the similarity between two strings
    def similarity(self, string1, string2):
        # Calculate the Levenshtein distance between the two strings
        distance = self.levenshtein_distance(string1, string2)

        # Calculate the similarity between the two strings
        similarity = 1 - (distance / max(len(string1), len(string2)))

        return similarity


    # This method is used to find the most similar word in a list of words to a given word
    def most_similar_word(self, word, words):
        # Initialize the most similar word and its similarity score
        most_similar_word = None
        max_similarity = 0

        # Iterate through the list of words
        for w in words:
            # Calculate the similarity between the given word and the current word
            similarity = self.similarity(word, w)

            # Update the most similar word and its similarity score if the current word is more similar
            if similarity > max_similarity:
                most_similar_word = w
                max_similarity = similarity

        return most_similar_word


    def is_similar(self, word1, word2, threshold):
        # Calculate the similarity between the two words
        similarity = self.similarity(word1, word2)

        # Check if the similarity is above the threshold
        if similarity >= threshold:
            return True
        else:
            return False



levenshtein_method = Levenshtein_Method()
word = "Horse"
words = ["", "Hre","arata", "jojoj", "se"]
most_similar_word = levenshtein_method.most_similar_word(word, words)
print(f"The most similar word to '{word}' is '{most_similar_word}'")


#After tests is_similar marks the word as is_similar only if 2 letters are different from the original word
word1 = "Brozyniak"
word2 = "Brozniak"
word3 = "Borozyniakos"
threshold = 0.8


is_similar1 = levenshtein_method.is_similar(word1, word2, threshold)
print(f"Are '{word1}' and '{word2}' similar? {is_similar1}")


is_similar2 = levenshtein_method.is_similar(word1, word3, threshold)
print(f"Are '{word1}' and '{word3}' similar? {is_similar2}")





