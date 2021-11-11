# 12/30
def reverse(x):
        """
        :type x: int
        :rtype: int
        """
        curr = abs(x)
        res = 0
        while curr > 0:
            # pull
            least = curr % 10
            curr = curr // 10
            # push
            res = res * 10 + least
            if res > (2**31):
                return 0
        if x < 0:
            res = 0-res
        return res

# Main
test = reverse(-2147483412)
assert(test==-2143847412)