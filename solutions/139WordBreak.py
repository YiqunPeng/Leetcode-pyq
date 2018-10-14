class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordDict = set(wordDict)
        n = len(s)
        dp = [False] * n
        
        for i in range(n):
            if s[:i+1] in wordDict:
                dp[i] = True
            else:
                dp[i] = any(dp[j] and s[j+1:i+1] in wordDict for j in range(i))
        
        return dp[-1]