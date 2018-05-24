class Solution:
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        word_to_id, id_to_word = {}, {}
        word_to_father = {}
        
        def find(w):
            if word_to_father[w] == word_to_id[w]:
                return word_to_father[w]
            else:
                word_to_father[w] = find(id_to_word[word_to_father[w]])
                return word_to_father[w]
            
        
        def unite(w1, w2):
            f_w1, f_w2 = find(w1), find(w2)
            if f_w1 == f_w2:
                return 
            word_to_father[id_to_word[f_w2]] = f_w1            
            
        
        w_id = 0
        
        len1, len2 = len(words1), len(words2)
        if len1 != len2: return False
        
        for w1, w2 in pairs:
            if w1 not in word_to_id:
                word_to_id[w1] = w_id
                word_to_father[w1] = w_id
                id_to_word[w_id] = w1
                w_id += 1
            if w2 not in word_to_id:
                word_to_id[w2] = w_id
                word_to_father[w2] = w_id
                id_to_word[w_id] = w2
                w_id += 1
            unite(w1, w2)
        
        for i in range(len1):
            w1, w2 = words1[i], words2[i]
            if w1 == w2: continue
            if w1 not in word_to_id or w2 not in word_to_id:
                return False
            if find(w1) != find(w2):
                return False
        
        return True
        
        
        