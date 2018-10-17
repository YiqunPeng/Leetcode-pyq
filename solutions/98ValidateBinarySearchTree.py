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
    # def isValidBST(self, root, min_v = -sys.maxsize, max_v = sys.maxsize):
    #     """
    #     :type root: TreeNode
    #     :rtype: bool
    #     """
    #     if not root: return True
    #     if root.val <= min_v or root.val >= max_v: return False

    #     if root.left and root.left.val >= root.val: return False
    #     if root.right and root.right.val <= root.val: return False

    #     return self.isValidBST(root.left, min_v, root.val) and self.isValidBST(root.right, root.val, max_v)        