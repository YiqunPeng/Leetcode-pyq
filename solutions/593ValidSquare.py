class Solution:
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        p = [p1, p2, p3, p4]
        
        sd = []
        for i in range(4):
            for j in range(i+1, 4):
                sd.append((p[i][0]-p[j][0])**2+(p[i][1]-p[j][1])**2)
        sd.sort()
        
        if sd[0] == 0 or sd[0] != sd[3]:
            return False
        if sd[4] != sd[5]:
            return False
        if sd[0] + sd[1] != sd[4]:
            return False
    
        return True