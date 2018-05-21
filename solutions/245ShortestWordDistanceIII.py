class Solution:
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        w1, w2 = [], []
        for i in range(len(words)):
            if words[i] == word1:
                w1.append(i)
            if words[i] == word2:
                w2.append(i)
        
        ans = sys.maxsize
        
        if word1 == word2:
            for i in w1:
                for j in w1:
                    if i == j: continue
                    ans = min(ans, abs(i-j))
        else:
            for i in w1:
                for j in w2:
                    ans = min(ans, abs(i-j))
        
        return ans