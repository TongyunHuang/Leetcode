# MM/DD 01/09

# Method
def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    symbol_dict = {'I':1, 'V':5, 'X':10,'L':50, 'C':100, 'D':500, 'M':1000}
    length = len(s)
    num = 0
    i = 0
    while i < length:
        add = 0
        # no subtraction
        if i == length - 1 or symbol_dict[s[i]] >= symbol_dict[s[i+1]]:
            add = symbol_dict[s[i]]
            i += 1
        # subtraction
        else:
            add = symbol_dict[s[i+1]] - symbol_dict[s[i]]
            i += 2
        num += add
    return num

# Test
test = romanToInt('MCMXCIV')
assert(test==1994)
print(test)