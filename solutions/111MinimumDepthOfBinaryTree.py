from queue import Queue

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        
        q = Queue()
        q.put((root, 1))
        while not q.empty():
            node, depth = q.get()
            if not node.left and not node.right:
                return depth
            if node.left:
                q.put((node.left, depth+1))
            if node.right:
                q.put((node.right, depth+1))
        
        