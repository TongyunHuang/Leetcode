class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # build a DP array with size m x n
        DP = [[0 for j in range(n)] for i in range(m)]
        # Base case: DP[0,0] = grid[0,0]
        DP[0][0] = grid[0][0]
        # Inductive: DP[i,j] = MIN(DP[i-1,j], DP[i,j-1]) + grid[i,j]
        topVal, leftVal = 100000, 100000
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                topVal = 100000 if i - 1 < 0 else DP[i-1][j]
                leftVal = 100000 if j - 1 < 0 else DP[i][j-1]
                DP[i][j] = min(topVal, leftVal) + grid[i][j]
        return DP[m-1][n-1]
