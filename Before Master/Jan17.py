def getRow(rowIndex):
    """
    :type rowIndex: int
    :rtype: List[int]
    """
    if rowIndex == 0:
        return [1]
    elif rowIndex == 1:
        return [1,1]
    else:
        prev = [1,1]
        for i in range(2,rowIndex +1):
            print(i, prev)
            subList = [1]* (i+1)
            for j in range(1, i):
                print("j = " + str(j))
                subList[j] = prev[j-1] + prev[j]
            prev = subList
            
        return prev

# Test

test = getRow(3)
print('your answer:')
print(test)

print('Compiler feedback:________')