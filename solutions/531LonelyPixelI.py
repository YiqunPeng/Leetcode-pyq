class Solution:
    def findLonelyPixel(self, picture):
        """
        :type picture: List[List[str]]
        :rtype: int
        """       
        if not picture or not picture[0]: return 0
        
        size = [len(picture), len(picture[0])]
        row_b, col_b = [0] * size[0], [0] * size[1]
        
        for i in range(size[0]):
            for j in range(size[1]):
                if picture[i][j] == 'B':
                    col_b[j] += 1
                    row_b[i] += 1
        
        ans = 0
        
        for i in range(size[0]):
            for j in range(size[1]):
                if picture[i][j] == 'B':
                    if col_b[j] == 1 and row_b[i] == 1:
                        ans += 1
        
        return ans
                    