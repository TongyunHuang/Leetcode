# 12/30
def findNumbers(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    return sum([len(str(n)) %2 ==0 for n in nums])

test = findNumbers([12,345,2,6,7896])
assert(test==2)
print(test)