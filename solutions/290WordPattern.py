class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = str.split(' ')
        w_len = len(words)
        p_len = len(pattern)
        
        if w_len != p_len: return False
        
        p_dic = {}
        w_dic = {}
        for i in range(p_len):
            if pattern[i] not in p_dic:
                p_dic[pattern[i]] = words[i]
            else:
                if words[i] != p_dic[pattern[i]]:
                    return False
            if words[i] not in w_dic:
                w_dic[words[i]] = pattern[i]
            else:
                if pattern[i] != w_dic[words[i]]:
                    return False
        
        return True
        
