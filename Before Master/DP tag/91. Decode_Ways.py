# 99, 85
class Solution:
    def numDecodings(self, s: str) -> int:
        def numInRange(substr: str) -> bool:

            # # check not start with 0
            if substr[0] == '0':
                return False
            # check if the numerical value of substr is btw 1-26,
            if int(substr) <= 26 and int(substr) >= 1:
                return True
            return False

        # DP array of size len(s)
        if len(s) < 1:
            return 0
        DP = [1 for i in range(len(s))]
        # Base case: len = 1: when s != '0', DP[0] = 1, len2 =
        if numInRange(s[0]):
            DP[0] = 1
        else:
            return 0

        # DP[i] = DP[i-2] +DP[i-1]
        splitBefore, notSplit = 0, 0
        for i in range(1, len(s)):
            # if s[i] in range, splitBefore = DP[i-1]
            splitBefore = 0 if not numInRange(s[i]) else DP[i-1]

            # if s[i-1] in range, notSplit = DP[i-2]
            if i == 1:
                notSplit = 0 if not numInRange(s[i-1:i+1]) else 1
            else:
                notSplit = 0 if not numInRange(s[i-1:i+1]) else DP[i-2]

            DP[i] = splitBefore + notSplit
            if DP[i] == 0:
                return 0

        return DP[len(s)-1]
