# 12/30
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    hTable = {}
    for i in range(len(nums)):
        n = nums[i]
        find = target - n
        if find in hTable:
            return [i,hTable[find]]
        hTable[n] = i

# Main
test = twoSum([2,7,11,11,15],9)
assert(test==[0,1])
print(test)