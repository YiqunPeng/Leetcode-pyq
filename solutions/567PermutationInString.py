class Solution:
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        s1_dic, s2_dic = {}, {}
        
        if len(s1) > len(s2): return False
        
        for c in s1:
            s1_dic[c] = s1_dic.get(c, 0) + 1
        
        for i in range(len(s1)):
            s2_dic[s2[i]] = s2_dic.get(s2[i], 0) + 1
        
        if s1_dic == s2_dic: return True
        
        for i in range(len(s1), len(s2)):
            s2_dic[s2[i]] = s2_dic.get(s2[i], 0) + 1
            s2_dic[s2[i-len(s1)]] -= 1
            if s2_dic[s2[i-len(s1)]] == 0:
                del s2_dic[s2[i-len(s1)]]
            if s1_dic == s2_dic:
                return True
            
        return False