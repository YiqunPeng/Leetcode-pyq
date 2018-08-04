class Solution:
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        A, Z = ord('A'), ord('Z')
        
        ans = ''
        for s in str:
            if A <= ord(s) <= Z:
                ans += chr(ord(s) - A + ord('a'))
            else:
                ans += s
        
        return ans
        