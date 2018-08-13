class Solution:
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        min_x, max_x = sys.maxsize, -sys.maxsize
        p_dict = collections.defaultdict(int)
        
        for p in points:
            min_x = min(min_x, p[0])
            max_x = max(max_x, p[0])
            p_dict[(p[0], p[1])] += 1
        
        symm = (min_x + max_x) / 2
        
        for p in points:
            if p[0] == symm: 
                p_dict[(p[0], p[1])] -= 1  
            elif (2 * symm - p[0], p[1]) in p_dict:
                p_dict[(2 * symm - p[0], p[1])] -= 1
            else:
                return False

        return True        
        