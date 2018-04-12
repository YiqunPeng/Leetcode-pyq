class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        max_w = int(area ** 0.5)
        for i in xrange(max_w, 0, -1):
            if area % i == 0:
                return [area/i, i]