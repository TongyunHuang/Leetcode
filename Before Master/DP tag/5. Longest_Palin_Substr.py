'''
5. Longest Palindromic Substring
'''


class Solution(object):
    """
    == Approach 3: Dynamic Programming ==
    * Consider the case "ababa". If we already knew that "bab" is a palindrom it is   obvious that "ababa" must be palindrome since the two left and righend letters are    the same
    * We define P(i,j) is true if the substring Si...Sj is a palindrome; false otherwise.
    * Then P(i,j) = ( P(i+1, j-1) and Si =Sj )
    * The base cases are: P(i,i) = true; P(i+1) = (Si==Si+1)
    """
    # Time exceed limit

    def longestPalindrome3(self, s):
        rows, cols = len(s), len(s)
        maxi, maxj, maxlen = 0, 0, 0
        arr = [[0 for i in range(cols)] for j in range(rows)]
        for i in range(len(s)):
            arr[i][i] = True
            if i-1 < 0:
                continue
            arr[i][i-1] = (s[i] == s[i-1])
            if 1 > maxlen and arr[i][i-1]:
                maxi, maxj, maxlen = i, i-1, 1
            if i-2 < 0:
                continue
            j = i-2
            while j >= 0:
                arr[i][j] = True if arr[i-1][j+1] and (s[i] == s[j]) else False
                if arr[i][j] and i-j > maxlen:
                    maxi, maxj, maxlen = i, j, i-j
                j -= 1
        return s[maxj:maxi+1]

    """
    == Approach 4: Expand Around Center
    # Go over all possible combination of center of palindrome, there are 2n-1 of them
    """

    def longestPalindrome4(self, s):
       # define subfunction
       def checkCenter(i, j):
            length = 0
            while i >= 0 and j < len(s) and s[i] == s[j]:
                length = j-i
                i -= 1
                j += 1
            return length, i+1, j-1

        # Main Code
        maxlen, maxi, maxj = 0, 0, 0
        for i in range(len(s)-1):
            currLen, curri, currj = checkCenter(i, i)
            # xprint(currLen, curri, currj)
            if currLen > maxlen:
                maxlen, maxi, maxj = currLen, curri, currj
            currLen, curri, currj = checkCenter(i, i+1)
            if currLen > maxlen:
                maxlen, maxi, maxj = currLen, curri, currj

        return s[maxi:maxj+1]

    
