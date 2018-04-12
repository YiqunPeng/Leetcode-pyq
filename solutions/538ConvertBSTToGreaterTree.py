# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root: return []
        gtr_root = TreeNode(root.val + self.sum_a_tree(root.right))
        
        return self.get_gtr_tree(gtr_root, root)
    
    def get_gtr_tree(self, gtr_root, root):
        if root.left:
            gtr_root.left = TreeNode(root.left.val)
            gtr_root.left.val = root.left.val + gtr_root.val + self.sum_a_tree(root.left.right)
            self.get_gtr_tree(gtr_root.left, root.left)
        if root.right:
            gtr_root.right = TreeNode(root.right.val)
            gtr_root.right.val = gtr_root.val - root.val - self.sum_a_tree(root.right.left)
            self.get_gtr_tree(gtr_root.right, root.right)
        return gtr_root
    
    def sum_a_tree(self, root):
        if not root: return 0
        sum = 0
        if root.left:
            sum += self.sum_a_tree(root.left)
        sum += root.val
        if root.right:
            sum += self.sum_a_tree(root.right)
        return sum