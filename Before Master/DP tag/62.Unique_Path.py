import math


class Solution(object):
    def uniquePaths1(self, m, n):
        """
        ==Approach1: DP==
        n^2, n^2
        """

        # f(m,n) = f(m-1,n) + f(m, n-1), f(1,1) = 0, f(1,#) = 1, f(#,1) = 1
        dp = [[1 for j in range(m)] for i in range(n)]
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[n-1][m-1]

    def uniquePaths2(self, m, n):
        """
        ==Approach2: combination==
        it takes m+n steps to go from start to end
        in these m+n steps, we choose m or n steps to be right or down
        so the number of unique path  = (m+n) choose m  || (m+n) choose n
        (m+n) choose m = (m+n)! / [m!n!]
        n, 1
        """
        numerator = math.factorial(m+n-2)
        print(numerator)
        denominator = math.factorial(m-1) * math.factorial(n-1)
        print(denominator)
        num = numerator/denominator
        return num
