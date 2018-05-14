class Solution:
    def minDistance(self, height, width, tree, squirrel, nuts):
        """
        :type height: int
        :type width: int
        :type tree: List[int]
        :type squirrel: List[int]
        :type nuts: List[List[int]]
        :rtype: int
        """
        ans = 0
        
        s2n_max = -sys.maxsize

        for [x, y] in nuts:
            s2n = abs(squirrel[0]-x) + abs(squirrel[1]-y)
            t2n = abs(tree[0]-x) + abs(tree[1]-y)
            
            if s2n_max < t2n - s2n:
                s2n_max = t2n - s2n
            ans += t2n * 2
        
        return ans - s2n_max