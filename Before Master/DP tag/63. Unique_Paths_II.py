class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # 1. count grid size, get list of obstacles indexes
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        obstacles = []
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    obstacles.append((j, i))
                    if i == 0 and j == 0:
                        return 0
        # 2. calculate
        l = [[1 for j in range(m)] for i in range(n)]

        for i in range(n):
            for j in range(m):
                if (i, j) in obstacles:
                    l[i][j] = 0
                elif i == 0:
                    l[i][j] = l[i][j-1]
                elif j == 0:
                    l[i][j] = l[i-1][j]
                elif i == 0 and j == 0:
                    l[i][j] = 1
                else:
                    l[i][j] = l[i-1][j] + l[i][j-1]
        # print(l)
        return l[n-1][m-1]
