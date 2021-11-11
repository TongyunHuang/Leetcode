'''
* Fist conside how to get the result f(n) from previous result f(0)...f(n-1).
* Actually, the result f(n) will be put an extra () pair to f(n-1). 
* Let the "(" always at the first position
** To produce a valid result, we can only put ")" in a way that there will be i pairs "()" inside the extra "()" and n - 1 - i pairs "()" outside the extra "()"

* Consider and example to get clear view
** f_0: None
** f_1: '(' f_0 ')'
** f_2: '(' f_0 ')'f_1 + '(' f_1 ')'f_0
** f_3: '(' f_0 ')'f_2 + '(' f_1 ')'f_1 + '(' f_2 ')'f_0
** f_n: '(' f_0 ')'f_{n-1} + '(' f_1 ')'f_{n-2} + ... + '(' f_{n-2} ')'f_1 + '(' f_{n-1} ')'f_0 
'''


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # 1. Base case: None when n = 0, None, when n=1 ()
        l = [[''], ["()"]]

        # 2. f_n = '('f_0')'f_{n-1} + '('f_1')'f_{n-2} + ... + '('f_{n-2}')'f_1 + '('f_{n-1}')'f_0
        for k in range(2, n+1):  # fill up memorization array
            currL = []
            for i in range(0, k):
                j = k-1-i
                for firItem in l[i]:
                    for sedItem in l[j]:
                        newItem = '(' + firItem + ')' + sedItem
                        currL.append(newItem)
            l.append(currL)
        return l[n]
