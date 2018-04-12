class Solution:
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        points_len = len(points)
        lengths = [[0 for i in range(points_len)] for j in range(points_len)]

        for i in range(points_len):
            for j in range(i+1, points_len):
                lengths[i][j] = math.sqrt((points[i][0]-points[j][0])**2+(points[i][1]-points[j][1])**2)
                
        ans = 0
        
        for i in range(points_len):
            for j in range(i+1, points_len):
                for k in range(j+1, points_len):
                    s = (lengths[i][j] + lengths[i][k] + lengths[j][k]) / 2.0
                    area = s * (s-lengths[i][j]) * (s-lengths[i][k]) * (s-lengths[j][k])
                    ans = max(ans, area)

        return math.sqrt(ans)