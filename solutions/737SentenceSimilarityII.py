class Solution:
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        father = {}
        
        def find(w):
            if father[w] == w:
                return w
            else:
                father[w] = find(father[w])
                return father[w]

        def unite(w1, w2):
            f_w1, f_w2 = find(w1), find(w2)
            if f_w1 != f_w2:
                father[f_w2] = find(f_w1)         

        len1, len2 = len(words1), len(words2)
        if len1 != len2: return False
        
        for w1, w2 in pairs:
            if w1 not in father:
                father[w1] = w1
            if w2 not in father:
                father[w2] = w2
            unite(w1, w2)
        
        for i in range(len1):
            w1, w2 = words1[i], words2[i]
            if w1 == w2: continue
            if w1 not in father or w2 not in father:
                return False
            if find(w1) != find(w2):
                return False
        
        return True