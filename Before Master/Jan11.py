# Jan 11

# 53. Maximum Subarray
def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    maxSum, maxIdx, arrSum, arrIdx = nums[0], 0, 0, 0
    L = []
    for i in range(len(nums)):
        if i == 0:
            L.append((0, nums[i]))
        else:
            newSum = L[i-1][1] + nums[i]
            # new start
            if nums[i] > newSum:
                arrSum ,arrIdx = nums[i], i
                L.append((arrIdx,arrSum))
            # append the subarr
            else:
                arrSum, arrIdx = newSum, L[i-1][0]
                L.append((L[i-1][0], arrSum))
            if arrSum > maxSum:
                maxSum, maxIdx = arrSum, arrIdx
    return maxSum

# 58. Length of Last Word
def lengthOfLastWord( s):
    """
    :type s: str
    :rtype: int
    """
    i = len(s)-1
    length = 0
    while i >= 0:
        if s[i] != ' ':
            length += 1
        elif length != 0:
            break
        i -= 1
    return length

# 66. Plus One
def plusOne( digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    i = len(digits) -1
    add = 1
    while i >= 0:
        if digits[i] + 1 == 10:
            digits[i] = 0
            if i == 0:
                digits.insert(0,1)
        else:
            digits[i] = digits[i] +1
            break
        i -= 1
    return digits

# 67. Add Binary
def addBinary( a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    carry = 0
    result = ''
    a, b = list(a), list(b)
    while a or b or carry:
        if a:
            carry += int(a.pop())
        if b:
            carry += int(b.pop())
        result += str(carry % 2)
        carry //= 2
    return result[::-1]

# 69. Sqrt(x)
def mySqrt( x):
    """
    :type x: int
    :rtype: int
    """
    left, right = 0, x
    res = 0
    while right-left>1:
        mid = (left + right)//2
        if mid* mid < x:
            left = mid
        else:
            right = mid
    if right* right <= x:
        return right
    return left

# 70. Climbing Stair
def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """
    # (even ,odd)
    L = []
    for i in range(n):
        if i == 0:
            L.append((0,1))
        else:
            even = L[i-1][1]
            odd = L[i-1][0] + L[i-1][1]
            L.append((even, odd))
    return L[-1][0] + L[-1][1]
# Test

test67 = addBinary('1010', '1011')
print('your answer:')
print(test67)
print('Compiler feedback:________')
assert(test67=='10101')
