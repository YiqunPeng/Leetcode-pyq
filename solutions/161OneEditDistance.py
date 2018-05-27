class Solution:
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_len, t_len = len(s), len(t)
        
        if abs(s_len - t_len) > 1: return False
        
        s_p, t_p = 0, 0
        
        dis = 0
        
        while s_p < s_len and t_p < t_len:
            if s[s_p] == t[t_p]:
                s_p += 1
                t_p += 1
                continue
            else:
                if dis == 1:
                    return False
                else:
                    dis += 1
                    if s_len == t_len:
                        s_p += 1
                        t_p += 1
                    elif s_len > t_len:
                        s_p += 1
                    else:
                        t_p += 1
        
        return (dis + s_len + t_len - s_p - t_p) == 1

