# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        arr = []
        self.traversal(root, arr)
        sub = [arr[i+1]-arr[i] for i in xrange(len(arr)-1)]
        return min(sub)
        
    def traversal(self, root, arr):
        if root.left:
            self.traversal(root.left, arr)
        if root:
            arr.append(root.val)
        if root.right:
            self.traversal(root.right, arr)