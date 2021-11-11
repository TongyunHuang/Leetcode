class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = []
        for i in range(len(triangle)):
            dp.append([0 for j in range(len(triangle[i]))])
            for j in range(len(triangle[i])):
                # Base case: top of the triangle
                if i == 0:
                    dp[i][j] = triangle[i][j]
                # if i-1 is 0 or j is 0 or j ==len(triangle[i])-1, no choice
                elif j == 0:
                    dp[i][j] = triangle[i][j] + dp[i-1][j]
                elif j == len(triangle[i]) - 1:
                    dp[i][j] = triangle[i][j] + dp[i-1][j-1]
                # choose the smaller one if possible
                else:
                    dp[i][j] = triangle[i][j] + min(dp[i-1][j-1], dp[i-1][j])

        h = len(triangle) - 1
        # print(dp)
        return min(dp[h])
