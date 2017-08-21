class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        ans = 0
        pos = 0
        for greed in g:
            while pos < len(s):
                if greed <= s[pos]:
                    ans += 1
                    pos += 1
                    break
                else:
                    pos += 1
            if pos >= len(s):
                return ans
        return ans
