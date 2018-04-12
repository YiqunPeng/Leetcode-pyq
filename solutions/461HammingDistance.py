class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        cnt = 0
        while x!=0 or y!=0:
            if x%2 != y%2:
                cnt += 1
            x = x // 2
            y = y // 2
        return cnt