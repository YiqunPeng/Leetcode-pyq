class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        new_s = s + t
        ans = 0
        for letter in new_s:
            ans ^= ord(letter)
        
        return chr(ans)