class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        s_len = len(s)
        
        dp = [0] * (s_len + 1)
        if s[0] in wordDict:
            dp[1] = 1
        else:
            dp[1] = 0
        
        for i in range(1, s_len+1):
            if s[0:i] in wordDict:
                dp[i] = 1
                continue
            for j in range(0, i):
                if dp[j] == 1:
                    if s[j:i] in wordDict:
                        dp[i] = 1
                        break
        
        return dp[-1] == 1