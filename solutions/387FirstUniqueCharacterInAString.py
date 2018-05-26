class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        for c in s:
            if c in dic:
                dic[c] += 1
            else:
                dic[c] = 1
        
        for i, c in enumerate(s):
            if dic[s[i]] == 1:
                return i
        
        return -1
            
