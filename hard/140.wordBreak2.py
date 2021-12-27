class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        """
        Idea:
        find the corresponding substring index in s
        store in a dict with starting index as the key
        """
        # fill up dp
        dp = [None for i in range(len(s))]
        for i in range(len(s)):
            for k,w in enumerate(wordDict):
                j = i+len(w)-1
                end = None if j+1>= len(s) else j+1
                if j <= len(s)-1 and s[i:end]== w:
                    if dp[i] is None:
                        dp[i] = [(j,k)]
                    else:
                        dp[i].append((j,k))
        print(dp)
        # construct outout
        return None
        
        
                    