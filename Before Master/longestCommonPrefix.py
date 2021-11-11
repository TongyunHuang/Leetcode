# MM/DD 01/09

# Method
def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    num_str = len(strs)
    index = 0
    prefix = ""
    # Edge case
    if num_str == 0:
        return index
    elif num_str == 1:
        return strs[0]
    # Most case
    comp_str = strs[0]
    while index < len(comp_str):
        comp = comp_str[index]
        for j in range(1,num_str):
            if index == len(strs[j]):
                return prefix
            elif strs[j][index]!= comp:
                return prefix
        index += 1
        prefix = prefix + comp
        print(prefix) 
    return prefix

# Test
test = longestCommonPrefix(['flowers','flowers','flowers'])
print('your answer:')
print(test)
print('Compiler feedback:________')
assert(test=='flowers')
