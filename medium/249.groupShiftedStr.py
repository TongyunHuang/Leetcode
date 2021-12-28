class Solution:
    # ['abc','bcd','cde','ceg', 'egj'] -> [['abc','bcd','cde']['ceg', 'egj']]
    def diffArr(self, s):
        if len(s) == 1: return ''
        res = ''
        for i in range(1,len(s)):
            diff = ord(s[i]) - ord(s[i-1])
            diff = 26+diff if diff < 0 else diff
            res += str(diff)
            res += ' '
        return res[:-1]
            
        
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        """
        strings in the same group has 2 equivalent property:(1) has same length;(2)diff betw char are same
        """
        d = {}
        res = []
        for i in range(len(strings)):
            arr = self.diffArr(strings[i])
            if d.get(arr,None) is not None:
                d[arr].append(strings[i])
            else:
                d[arr] = [strings[i]]
                
        for key in d:
            res.append(d[key])
        return res