class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == []: return ''
        min_str = ''
        min_len = strs[0]
        for str in strs:
            if len(str) < min_len:
                min_str = str
                min_len = len(str)

        while min_str != '':
            print(min_str)
            flag = 0
            for str in strs:
                if not str.startswith(min_str):
                    min_str = min_str[0:-1]
                    flag = 1
                    break
            if flag == 0:
                return min_str
        
        return min_str