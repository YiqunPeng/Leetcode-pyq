"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
class Solution:
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        def construct_subtree(x1, y1, x2, y2):
            root = Node(None, False, None, None, None, None)
            
            s = 0
            for i in range(x1, x2):
                for j in range(y1, y2):
                    if grid[i][j] == 1: s += 1
            
            if s == (x2 - x1) * (y2 - y1):
                root.val = True
                root.isLeaf = True
            elif s == 0:
                root.val = False
                root.isLeaf = True
            else:
                root.topLeft = construct_subtree(x1, y1, (x1+x2)//2, (y1+y2)//2)
                root.topRight = construct_subtree(x1, (y1+y2)//2, (x1+x2)//2, y2)
                root.bottomLeft = construct_subtree((x1+x2)//2, y1, x2, (y1+y2)//2)
                root.bottomRight = construct_subtree((x1+x2)//2, (y1+y2)//2, x2, y2)
            return root
            
        
        return construct_subtree(0, 0, len(grid), len(grid))