class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        mode = 's'
        for c in s:
            if c == ' ' and mode == 'c':
                ans += 1
                mode = 's'
            elif c == ' ':
                mode = 's'
            else:
                mode = 'c'
        if mode == 'c':
            return ans + 1
        return ans