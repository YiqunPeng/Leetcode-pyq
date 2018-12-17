class Solution:
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        def is_ordered(word1, word2):
            p1, p2 = 0, 0
            while p1 < len(word1) and p2 < len(word2):
                if dictionary[word1[p1]] < dictionary[word2[p2]]:
                    return True
                elif dictionary[word1[p1]] > dictionary[word2[p2]]:
                    return False
                p1 += 1
                p2 += 1
                
            return len(word1) <= len(word2)
        
        
        dictionary = {}
        for idx, c in enumerate(order):
            dictionary[c] = idx
            
        for i in range(1, len(words)):
            if not is_ordered(words[i-1], words[i]): return False
        return True