class Solution:
    """
    Use quieckSect algorithm:
    - in the partition step, index of pivot decide final position of the element
    - our goal is find the pivot that is the Kth largest, i.e. pivot index  = k-1
    Randomization when choosing pivot may increase runtime
    """
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quickSelectK(nums, k, 0, len(nums)-1)
        
    def quickSelectK(self,nums, k, left, right):
        if left <= right:
            pivot = self.partition(nums, left, right)
            if pivot  == k-1:
                return nums[pivot]
            elif pivot > k-1:
                return self.quickSelectK(nums, k, left, pivot-1)
            else: # pivot < k-1
                return self.quickSelectK(nums, k, pivot+1, right)
        
        
    def partition(self, nums: List[int], start, end) -> int:
        pivot = start
        curr = start+1
        for i in range(start+1, end+1):
            if nums[i] > nums[pivot]:
                nums[curr], nums[i] = nums[i], nums[curr]
                curr += 1
        nums[curr-1], nums[pivot] = nums[pivot], nums[curr-1]
        pivot = curr-1
        return pivot
        