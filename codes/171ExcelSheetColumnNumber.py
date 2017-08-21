class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        s_list = list(s)
        s_list.reverse()
        for i in xrange(len(s_list)):
            ans += 26 ** i * (ord(s_list[i]) - ord('A') + 1)
        return ans