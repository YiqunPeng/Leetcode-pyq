class Solution:
    def areSentencesSimilar(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if len(words1) != len(words2): return False
        length = len(words1)
        
        dic = {}
        for pair in pairs:
            if pair[0] not in dic:
                dic[pair[0]] = [pair[1]]
            else:
                dic[pair[0]].append(pair[1])
            if pair[1] not in dic:
                dic[pair[1]] = [pair[0]]
            else:
                dic[pair[1]].append(pair[0])
        
        for i in range(length):
            if words1[i] == words2[i]: continue
            if words1[i] not in dic or words2[i] not in dic[words1[i]]:
                return False
        
        return True
        