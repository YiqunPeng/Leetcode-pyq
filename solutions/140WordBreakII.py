class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        ans = []
        s_len = len(s)
                
        dp = [[] for i in range(s_len + 1)]
        if s[0] in wordDict:
            dp[1] = [1]
        else:
            dp[1] = []
        
        for i in range(2, s_len+1):
            if s[0:i] in wordDict:
                dp[i] = [i]
            else:
                dp[i] = []
            for j in range(1, i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i].append(j)
                
        def backtracking(curr, pos):
            for i in dp[pos]:
                if i == pos:
                    ans.append(curr)
                else:
                    backtracking(curr[0:i]+' '+curr[i:], i)
        
        backtracking(s, s_len)

        return ans
                    
        