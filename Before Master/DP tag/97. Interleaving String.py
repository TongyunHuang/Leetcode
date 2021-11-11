class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # helper function to avoid confusion on index
        def getChar(s: str, idx: int) -> str:
            return s[idx-1]
        if len(s1) + len(s2) != len(s3):
            return False
        # 2D array for memorization
        dp = [[False for j in range(len(s2)+1)]for i in range(len(s1)+1)]
        for i in range(len(s1)+1):
            for j in range(len(s2) + 1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                elif i == 0:
                    if dp[i][j-1] == True and getChar(s2, j) == getChar(s3, i+j):
                        dp[i][j] = True
                elif j == 0:
                    if dp[i-1][j] and getChar(s1, i) == getChar(s3, i+j):
                        dp[i][j] = True
                else:
                    if (dp[i-1][j] and getChar(s1, i) == getChar(s3, i+j)) or (dp[i][j-1] and getChar(s2, j) == getChar(s3, i+j)):
                        dp[i][j] = True
        return dp[len(s1)][len(s2)]
