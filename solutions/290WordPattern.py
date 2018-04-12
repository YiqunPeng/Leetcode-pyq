class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str_list = str.split(' ')
        if len(str_list) != len(pattern): return False
        
        p_dict = {}
        for i in xrange(len(pattern)):
            if p_dict.has_key(pattern[i]):
                if p_dict[pattern[i]] != str_list[i]:
                    return False
            else:
                p_dict[pattern[i]] = str_list[i]
        
        s_dict = {}
        for i in xrange(len(str_list)):
            if s_dict.has_key(str_list[i]):
                if s_dict[str_list[i]] != pattern[i]:
                    return False
            else:
                s_dict[str_list[i]] = pattern[i]       
                
        return True