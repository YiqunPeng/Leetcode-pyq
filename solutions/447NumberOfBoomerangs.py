class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        ans = 0
             
        for p in points:
            dis_dict = {}
            for q in points:
                if p == q: 
                    continue
                x_d = p[0] - q[0]
                y_d = p[1] - q[1]
                dis_dict[x_d ** 2 + y_d ** 2] = 1 + dis_dict.get(x_d ** 2 + y_d ** 2, 0)
            for key in dis_dict:
                ans += dis_dict[key] * (dis_dict[key] - 1)
        
        return ans