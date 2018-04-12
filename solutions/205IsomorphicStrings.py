class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
                
        return self.map_string(s, t) and self.map_string(t, s)
    
    def map_string(self, s, t):
        iso_dict = {}       
        for i in xrange(len(s)):
            if iso_dict.has_key(s[i]):
                if t[i] != iso_dict[s[i]]:
                    return False
            else:
                iso_dict[s[i]] = t[i]
        return True