# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):  
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        arr = []
        self.traversal(root, arr)
        l, r = 0, len(arr)-1
        while l < r:
            if arr[l] + arr[r] == k:
                return True
            elif arr[l] + arr[r] < k:
                l += 1
            else:
                r -= 1
        return False        
        
    def traversal(self, root, arr):
        if root.left: self.traversal(root.left, arr)
        arr.append(root.val)
        if root.right: self.traversal(root.right, arr)