# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # iterative, inorder
    # time: O(n)
    # space: O(n)
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        
        pre = None
        stack = []

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if pre and root.val <= pre.val:
                return False
            else:
                pre = root
            root = root.right
        
        return True
        
    # recursive, inorder
    # time: O(n)
    # space: O(n)
    # def isValidBST(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: bool
    #     """
    #     def isValid(root, min_v, max_v):
    #         if not root: return True
    #         if root.val <= min_v or root.val >= max_v: return False
    #         return isValid(root.left, min_v, root.val) and isValid(root.right, root.val, max_v)

    #     if not root: return True
    #     return isValid(root, -sys.maxsize, sys.maxsize)
        


        
        
        
