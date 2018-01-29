class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def is_palind(s, l, r, flag):
            while l < r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    if flag == 1:
                        return is_palind(s, l+1, r, 0) or is_palind(s, l, r-1, 0)
                    else:
                        return False
            return True
            
            
        return is_palind(s, 0, len(s)-1, 1)