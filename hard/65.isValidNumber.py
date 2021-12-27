class Solution:
   
    # return true if char is digit [0-9] ->[48-57]
    def isDigit(self, c):
        asciiVal = ord(c)
        #print('c', c, 'val', asciiVal)
        return asciiVal <= 57 and asciiVal >= 48
    
    # return true if s is decimal
    def isDecimal(self,s):
        dotCnt = 0
        res = False
        if s[0] in {'+','-'}:
            s = s[1:]
        #print('decimal-s',s)
        if len(s) <= 1:return False
        for i in range(len(s)):
            if s[i] == '.':
                dotCnt += 1
                if dotCnt > 1:
                    return False
                
            elif self.isDigit(s[i]) == False:
                return False
            
            if i == len(s)-1:
                res = True
        return res
            
    
    # return true if s is an integer
    def isInteger(self,s):
        res = False
        if s[0] in {'+','-'}:
            s = s[1:]
        for i in range(len(s)):
            if self.isDigit(s[i]) == False:
                #print('isDigit ret false')
                return False
            if i == len(s)-1:
                #print('set to true')
                res = True
        return res
    
    
    # call from here
    def isNumber(self, s: str) -> bool:
        s = s.lower()
        if 'e' in s:
            arr = s.split('e')
            if (len(arr) == 2 and len(arr[0])>0 and len(arr[1])>0):
                
                return self.isNumber(arr[0]) and self.isInteger(arr[1])
        elif '.' in s:
            return self.isDecimal(s)
        else:
            return self.isInteger(s)
        return False
    
        