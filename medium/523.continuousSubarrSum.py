class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        """
        Follow dicussion sol - Idea:
        - Observation: if sum(nums[i:j])%k == 0, then sum(nums[i])%k =sum(nums[:j])%k
        - So we can just use a dict to keep track
        """
        dic = {0:-1}
        summ = 0
        for i,n in enumerate(nums):
            if k != 0:
                summ = (summ+n)%k
            else:
                summ += n
            if dic.get(summ, None) is None:
                dic[summ] = i
            else:
                if i - dic[summ] > 1:
                    return True
        return False