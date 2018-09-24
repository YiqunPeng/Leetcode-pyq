class Solution:
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l, h = 0, 0
        
        for c in s:
            if c == '(':
                l += 1
                h += 1
            elif c == ')':
                if l: l -= 1
                h -= 1
            else:
                if l: l -= 1
                h += 1
            
            if h < 0: return False
        
        return l == 0