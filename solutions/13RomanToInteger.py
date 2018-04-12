class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        
        ans = 0
        for i in xrange(len(s)-1):
            if roman_dict[s[i]] >= roman_dict[s[i+1]]:
                ans += roman_dict[s[i]]
            else:
                ans -= roman_dict[s[i]]
        return ans + roman_dict[s[-1]]