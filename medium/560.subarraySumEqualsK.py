class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        Idea:
        - Observation: if sum(nums[i:j]) == k, then sum(nums[:j]) - sum(nums[:i])
        - so we store sum(nums[:i]) in a hash table with key-sum, val-array of i
        - look for sum(nums[:i]) -k in each iteration
        """
        dic = {0:[-1]}
        summ = 0
        count = 0
        for i in range(len(nums)):
            summ += nums[i]
            if dic.get(summ-k, None) is not None:
                count += len(dic[summ-k])
            if dic.get(summ, None) is not None:
                dic[summ].append(i)
            else:
                dic[summ] = [i]
        # print(dic)
        return count
            