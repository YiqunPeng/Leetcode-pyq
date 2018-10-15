class Solution:
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        words_set = set(words)
        prefix = set()
        ans = []
        
        for w in words:
            if not w: continue
            n = len(w)
            dp = [False] * n
            for i in range(n):
                if w[:i+1] in prefix and w[i+1:] in words_set:
                    dp[-1] = True
                    break
                if w[:i+1] in words_set and i != n - 1:
                    dp[i] = True
                else:
                    dp[i] = any(dp[j] and w[j+1:i+1] in words_set for j in range(i))
            if dp[-1]: 
                prefix.add(w)
                ans.append(w)
        
        return ans