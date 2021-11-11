# 122. Best time to Buy and Sell Stocks
def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    if len(prices) <= 0:
        return 0
    if len(prices) ==2:
        if prices[1]-prices[0] >0:
            return prices[1]-prices[0]
        return 0
    total = 0
    localMin, localMax = prices[0], prices[0]
    profit = 0
    for i in range(1,len(prices)-1):
        if prices[i]< prices[i-1] and prices[i] <= prices[i+1]:
            localMin = prices[i]
        if prices[i] > prices[i-1] and prices[i] >= prices[i+1] :
            localMax = prices[i]
            print("localMax = " + str(localMax) + "; localMin = " + str(localMin))
            profit = localMax-localMin
            print("---profit = " + str(profit))
        if i== len(prices)-2 and prices[len(prices)-1] >= prices[i]:
            localMax = prices[i+1]
            print("localMax = " + str(localMax) + "; localMin = " + str(localMin))
            profit = localMax-localMin
            print("---profit = " + str(profit))
            
        if profit >0:
            total += profit
            localMin = localMax
        profit = 0
    return total

# 125. isPalindrome
def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    i, j = 0, len(s)-1
    while i <= j:
        print("s[i] = "+ s[i] + "; s[j] = " + s[j])
        if s[i].isalnum() and s[j].isalnum() :
            print("both alpha s[i] = "+ s[i] + "; s[j] = " + s[j])
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        elif s[i].isalnum():
            j -= 1
        elif s[j].isalnum():
            i += 1
        else:
            i += 1
            j -= 1 
    return True

# Test

test = isPalindrome(",,,,,,,,,,,,acva")
print('your answer:')
print(test)

print('Compiler feedback:________')           