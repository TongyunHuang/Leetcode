class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 1. check backward from the last index
        # 2. keep track of the smallest index that can reach this last index
        # 3. check whether there exist an index that can reach the smallest index
        # 4. if there exist a way to jump to the last index, the we should end with last = 0: we can jump to the last index from index 0
        n = len(nums)
        last = n-1
        for i in range(n-2, -1, -1):
            if (i + nums[i] >= last):
                last = i
        return last <= 0
        # time: 22 memo 55
