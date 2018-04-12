class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        if len(s) == 0: return ans
        
        mode = ' '
        for i in xrange(len(s)-1, -1, -1):
            if s[i] == ' ' and mode == 'c':
                return ans
            else:
                if s[i] != ' ':
                    ans += 1
            if (ord(s[i]) >= ord('A') and ord(s[i]) <= ord('Z')) or (ord(s[i]) >= ord('a') and ord(s[i]) <= ord('z')):
                mode = 'c'        
        
        return ans