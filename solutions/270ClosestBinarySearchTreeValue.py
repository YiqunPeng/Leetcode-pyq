# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.ans = -1
        self.diff = sys.maxsize
        self.found = False
    
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        def search(node, target):
            if self.found: return
            if not node: return
            if node.val == target:
                self.found = True
                self.diff = 0.
                self.ans = node.val
            else: 
                diff = abs(node.val - target)
                if self.diff > diff:
                    self.diff = diff
                    self.ans = node.val
                if node.val > target:
                    search(node.left, target)
                else:
                    search(node.right, target)

                    
        search(root, target)
        return self.ans
        
        
