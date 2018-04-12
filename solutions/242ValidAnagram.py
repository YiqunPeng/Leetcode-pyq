class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_dict = self.str2dict(s)
        t_dict = self.str2dict(t)
        
        if cmp(s_dict, t_dict) == 0:
            return True
        return False

    def str2dict(self, s):
        d = {}
        for c in s:
            if d.has_key(c):
                d[c] += 1
            else:
                d[c] = 1
        return d