'''
== Approach 2 ==
Since we are repeatedly calculating the same answer over and over again. The jumps required to reach for a given index on the path remains fixed and can be stored in dp array to avoid re-calculations.
'''


def jump(nums):
    # initialize all to max possible jumps + 1 denoting dp[i] hasn't been computed
    dp = [1001] * len(nums)
    return solve(nums, dp, 0)

#  recursive solver to find min jumps to reach end


def solve(nums, dp, pos):
    # when we reach end, return 0 denoting no more jumps required
    if(pos >= len(nums) - 1):
        return 0
    # number of jumps from pos to end is already calculated, so just return it
    if (dp[pos] != 1001):
        return dp[pos]
    # explore all possible jump sizes from current position. Store & return min jumps required
    for j in range(1, nums[pos]):
        dp[pos] = min(dp[pos], 1+solve(nums, dp, pos+j))
    return dp[pos]
