class Solution:
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        seen = set()
        ans = sys.maxsize
        
        for x1, y1 in points:
            for x2, y2 in seen:
                if (x1, y2) in seen and (x2, y1) in seen:
                    ans = min(ans, abs((x2-x1)) * abs((y2-y1)))
            seen.add((x1, y1))
        
        return ans if ans != sys.maxsize else 0        