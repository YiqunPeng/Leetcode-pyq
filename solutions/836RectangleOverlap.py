class Solution:
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        x1, y1, x2, y2 = rec1[0], rec1[1], rec1[2], rec1[3]
        x3, y3, x4, y4 = rec2[0], rec2[1], rec2[2], rec2[3]
        
        if x1 <= x3 < x2 and y1 <= y3 < y2:
            return True
        if x1 <= x3 < x2 and y1 <= y4 < y2:
            return True
        
        if x1 < x4 <= x2 and y1 < y4 <= y2:
            return True
        if x1 < x4 <= x2 and y1 < y3 <= y2:
            return True
    
        
        if x3 <= x1 < x4 and y3 <= y1 < y4:
            return True
        if x3 <= x1 < x4 and y3 <= y2 < y4:
            return True
        
        if x3 < x2 <= x4 and y3 < y2 <= y4:
            return True
        if x3 < x2 <= x4 and y3 < y1 <= y4:
            return True
        
        if x3 <= x1 < x4 and y1 <= y3 and x2 <= x4 and y2 >= y4:
            return True
        if x1 <= x3 < x2 and y3 <= y1 and x4 <= x2 and y4 >= y2:
            return True
            
        
        return False
        