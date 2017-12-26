class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        def dfs(sr, sc, oldColor, newColor, image):
            print(sr)
            print(sc)
            image[sr][sc] = newColor
            fx = [[sr-1,sc], [sr+1,sc], [sr,sc+1], [sr,sc-1]]
            n, m = len(image), len(image[0])
            for i in fx:
                n_sr, n_sc = i[0], i[1]
                if n_sr>=0 and n_sr<n and n_sc>=0 and n_sc<m and image[n_sr][n_sc]==oldColor:
                    dfs(n_sr, n_sc, oldColor, newColor, image)
        
        oldColor = image[sr][sc]
        if oldColor == newColor:
            return image
        
        dfs(sr, sc, oldColor, newColor, image)
        
        return image