class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if haystack == '' and needle == '': return 0
        
        n_len = len(needle)
        for i in xrange(len(haystack)-n_len+1):
            temp = haystack[i:(i+n_len)]
            if temp == needle:
                return i
            
        return -1