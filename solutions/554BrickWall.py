class Solution:
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        edge_dic = {}
        
        height = len(wall)
        
        for i in range(height):
            edge = 0
            for width in wall[i][0:-1]:
                edge += width
                edge_dic[edge] = edge_dic.get(edge, 0) + 1
        
        if edge_dic:
            return height - max(edge_dic.values())
        else:
            return height