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
        
        dic = collections.defaultdict(list)
        for pair in pairs:
            dic[pair[0]].append(pair[1])
            dic[pair[1]].append(pair[0])
        
        for i in range(length):
            if words1[i] == words2[i]: continue
            if words1[i] not in dic or words2[i] not in dic[words1[i]]:
                return False
        
        return True