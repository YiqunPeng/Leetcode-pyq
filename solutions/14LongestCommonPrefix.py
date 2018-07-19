class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs or not strs[0]: return ''
        
        ptr = 0
        ans = ''
        
        while True:
            if ptr >= len(strs[0]):
                return ans
            else:
                c = strs[0][ptr]
            for s in strs:
                if ptr >= len(s):
                    return ans
                if c != s[ptr]:
                    return ans
            ptr += 1
            ans += c
