class Solution:
  def threeSum(self, nums):
    res = []
    nums.sort()
    for i in range(len(nums)):
      if nums[i] > 0:
        break
      if i == 0 or nums[i-1] != nums[i]:
        self.twoSum(nums, i, res)
    return res

  def twoSum(self, nums, i, res):
    lo, hi = i+1, len(nums)-1
    while (lo < hi):
      sum = nums[i] + nums[lo] + nums[hi]
      if sum < 0:
        lo += 1
      elif sum > 0:
        hi -= 1
      else:
        res.append([nums[i]], nums[lo], nums[hi]])