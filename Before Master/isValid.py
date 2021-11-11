# MM/DD

# Description
'''
20. Valid Parentheses | Easy
    * Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
    * An input string is valid if:
    * Open brackets must be closed by the same type of brackets.
    * Open brackets must be closed in the correct order.
'''

# Method
def isValid( s):
    """
    :type s: str
    :rtype: bool
    """
    if len(s) % 2 != 0:
        return False
    left = ['(', '{', '[']
    pair = {'(':')','[':']','{':'}'}
    stack = []
    for i in range(len(s)):
        if s[i] in left:
            stack.append(s[i])
        else:
            if len(stack) != 0:
                sig = stack.pop(-1)
                if pair[sig] != s[i]:
                    return False
            else:
                return False
    if len(stack) != 0:
        return False
    return True

# Test

test = isValid("()[]{}")
print('your answer:')
print(test)
print('Compiler feedback:________')
assert(test==True)
