class LevenshteinDistance:

    def __init__(self):
        pass

    def calculate(self, str1, str2):

        m = len(str1) + 1
        n = len(str2) + 1


        dp = [[0 for _ in range(n)] for _ in range(m)]


        for i in range(1, m):
            dp[i][0] = i
        for j in range(1, n):
            dp[0][j] = j


        for i in range(1, m):
            for j in range(1, n):
                if str1[i - 1] == str2[j - 1]:
                    cost = 0
                else:
                    cost = 1
                dp[i][j] = min(dp[i - 1][j] + 1,
                               dp[i][j - 1] + 1,
                               dp[i - 1][j - 1] + cost)

        return dp[m - 1][n - 1]