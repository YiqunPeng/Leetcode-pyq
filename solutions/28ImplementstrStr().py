class Solution:
    # string
    # time: O(n * m) n -- len(haystack); m -- len(needle)
    # space: O(1)
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle: return 0
        if not haystack: return -1
        
        h_len, n_len = len(haystack), len(needle)
        
        for i in range(h_len - n_len + 1):
            if haystack[i:i+n_len] == needle:
                return i
        
        return -1
        
        