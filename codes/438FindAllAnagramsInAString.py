class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(p) > len(s): return []
        
        ans = []
        p_dict = {}
        for c in p:
            p_dict[c] = 1 + p_dict.get(c, 0)
        
        s_dict = {}
        for i in xrange(0, len(p)):
            s_dict[s[i]] = 1 + s_dict.get(s[i], 0)
        if s_dict == p_dict:
            ans.append(0)
        
        for i in xrange(1, len(s)-len(p)+1):
            s_dict[s[i-1]] -= 1
            s_dict[s[i+len(p)-1]] = 1 + s_dict.get(s[i+len(p)-1], 0)
            for key in list(s_dict):
                if s_dict[key] == 0:
                    s_dict.pop(key)
            if s_dict == p_dict:
                ans.append(i)
        
        return ans