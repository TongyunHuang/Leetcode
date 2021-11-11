# MM/DD Jan 10

# Description 26. remove duplicates
'''
* Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.
* Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
'''
# Method
def removeDuplicates( nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 0:
        return 0
    prev = nums[0]
    i = 1
    while True:
        if i > len(nums) - 1:
            break
        if nums[i] == prev:
            nums.pop(i)
        else:
            prev = nums[i]
            i += 1
    return len(nums), nums

# Method2 | Solution, slightly faster
def removeDuplicates2(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 0:
        return 0
    i = 0
    for j in range(1, len(nums)):
        if nums[i] != nums[j]:
            nums[i+1] = nums[j]
            i += 1
    nums = nums[: i+1]
    return i+1

# 27. Remove Element
def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i+= 1
        return i

# 28. Implement strStr()
def strStr( haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    if len(needle) == 0:
        return 0
    elif len(needle) > len(haystack):
        return -1
    index = -1
    for i in range(len(haystack)-len(needle)+1):
        index = i
        for j in range(len(needle)):
            if haystack[i] != needle[j] or i > len(haystack)-1:
                i = index
                index = -1
                break
            i += 1
        if index != -1:
            return index
    return index

# 35. Search Insert Position
def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    start, end = 0, len(nums)-1
    while start < end:
        mid = (start + end - 1)//2
        if nums[mid] == target:
            return mid
        elif target < nums[mid]:
            end = mid - 1
        else:
            start = mid + 1
    # now start = end
    if target <= nums[start]:
        return start
    else:
        return start+1

# 38. Count and Say
def countAndSay(n):
    """
    :type n: int
    :rtype: str
    """
    print("curr N = "+ str(n)+"---------")
    # Base Case
    if n == 1:
        print("return: 1##")
        return "1"
    # Recursive Case
    numStr = countAndSay(n-1)
    print("curr N = "+ str(n)+"---------" + "numStr = " + numStr)
    # Initialize
    if len(numStr) == 1:
        print("return: 11##")
        return "11"
    resL = ['1', numStr[0]]
    preFre =  1
    preDg = numStr[0] if len(numStr) > 1 else numStr
    i = 1
    idx = 1
    # pop and check
    while i < len(numStr):
        currDg = numStr[i]
        # if switch digit, append previous substr info to resStr
        if currDg != preDg:
            preDg = currDg
            preFre = 1
            resL.append(str(preFre))
            resL.append(preDg)
            idx += 2
        # if same digit, increment frequency
        else:
            preFre+=1
            resL[idx-1] = str(preFre)
            print(resL)

        i+=1
    resStr = ''.join(resL)
    print("return " + resStr +"##")
    return resStr   

# Test

test = countAndSay(4)
print('your answer:')
print(test)
print('Compiler feedback:________')
assert(test== '1211')
