class Solution:
    def validPalindrome(self, s, chance = 1):
        """
        :type s: str
        :rtype: bool
        """
        if not s: return True
        
        l, r = 0, len(s) - 1
        while l <= r and s[l] == s[r]:
            l += 1
            r -= 1
        
        if chance == 1:
            return self.validPalindrome(s[l+1:r+1], 0) or self.validPalindrome(s[l:r], 0)
        else:
            return l > r