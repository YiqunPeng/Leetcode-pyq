# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Master(object):
#    def guess(self, word):
#        """
#        :type word: str
#        :rtype int
#        """

class Solution(object):
    # minmax
    # time: O(n^2)
    # space: O(n)
    def findSecretWord(self, wordlist, master):
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """
        def match(s1, s2):
            res = 0
            for i in range(6):
                if s1[i] == s2[i]: res += 1
            return res
        
        def max_match(w):
            vals = [0] * 7
            for word in wordlist:
                vals[match(word, w)] += 1
            return max(vals)
        
        attempt = 0
        while attempt < 10:
            word, min_m = '', sys.maxsize
            for w in wordlist:
                m = max_match(w)
                if min_m > m:
                    min_m = m
                    word = w
            
            res = master.guess(word)
            if res == 6: return
            
            nxt_list = []
            for w in wordlist:
                if match(w, word) == res and w != word:
                    nxt_list.append(w)
            wordlist = nxt_list
            
            attempt += 1