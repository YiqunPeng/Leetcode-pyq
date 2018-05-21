class WordDistance:

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.dic = {}
        for i in range(len(words)):
            if words[i] in self.dic:
                self.dic[words[i]].append(i)
            else:
                self.dic[words[i]] = [i]
        

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        w1, w2 = self.dic[word1], self.dic[word2]
        res = sys.maxsize
        for i in w1:
            for j in w2:
                res = min(res, abs(i-j))
        return res

# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)