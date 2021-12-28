class Solution:
    def wordBreak(self, s, wordDict):
        """
        Idea:
        find the corresponding substring index in s
        store in a dict with starting index as the key
        """
        # fill up dp
        dp = [None for i in range(len(s)+1)]
        for i in range(len(s)):
            for k,w in enumerate(wordDict):
                j = i+len(w)
                end = None if j>= len(s) else j
                
                if j <= len(s) and s[i:end]== w:
                    
                    if dp[j] is None:
                        dp[j] = [(i,k)]
                    else:
                        dp[j].append((i,k))
        #print(dp)
        resArr = []
        self.dfs(dp, '', len(s), wordDict, resArr)
        return resArr

    def dfs(self, dp, resStr, idx, wordDict, resArr):
        if idx == 0 and dp[idx] is None:
            if len(resStr.strip()) > 0:
                resArr.append(resStr.strip())
            return
        if dp[idx] is None: return
        for p in range(len(dp[idx])):
            (i,k) = dp[idx][p]
            newStr = wordDict[k] + ' ' + resStr
            nexIdx = i
            if idx == 0:
                resArr.append(newStr.strip())
                return
            else:
                self.dfs(dp,newStr,nexIdx,wordDict, resArr)
            
            
        
        
                    