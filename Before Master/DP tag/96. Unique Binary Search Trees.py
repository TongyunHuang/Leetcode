class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0 for i in range(n+1)]
        dp[1] = 1

        for i in range(2, n+1):
            count = 0
            for j in range(i):
                k = i-1-j

                if k == 0 or j == 0:
                    count += dp[k] + dp[j]
                else:
                    count += dp[k] * dp[j]
                # print('count-', count, '; j-',j, '; k-', k," ;dp[k]: ",dp[k], " ;dp[j]: ",dp[j]  )
            dp[i] = count
        # print(dp)
        return dp[n]
