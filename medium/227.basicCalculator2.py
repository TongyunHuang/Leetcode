class Solution:
    # Sol 1: with stack
    
    def calculate(self, s: str) -> int:
        """
        traverse throught string s, if is digit, append
        if operator is in {+, -}, push to stack with sign
        else, pop from stack and calculate the value
        """
        s = s.strip()
        stack = []
        num = ''
        sign = ''
        for i in range(len(s)):
            if s[i] == ' ':continue
            
            if s[i].isdigit():
                num+=s[i]
            # is operator
            if not s[i].isdigit() or i ==len(s)-1:
                #handdle divide and multiply
                if sign in {'*', '/'}:
                    last = stack.pop(-1)
                    if sign =='*':
                        num = str(last*int(num))
                    else:
                        num = str(int(last/int(num)))
                    sign = ''
                #print(num)
                stack.append(int(sign+num))
                sign = ''
                if s[i] != '+':
                    sign = s[i]
                num = ''
            #print(stack)
        return sum(stack)
                
                    
                
            