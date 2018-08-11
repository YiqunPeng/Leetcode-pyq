class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s2t, t2s = {}, {}
        
        for i in range(len(s)):
            if s[i] not in s2t:
                s2t[s[i]] = t[i]
            elif s2t[s[i]] != t[i]:
                return False
            
            if t[i] not in t2s:
                t2s[t[i]] = s[i]
            elif t2s[t[i]] != s[i]:
                return False
        
        return True
            