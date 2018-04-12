# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        def preorder(root):
            if not root: return ''
            s = str(root.val)
            ls = preorder(root.left)
            rs = preorder(root.right)
            if ls == '' and rs == '':
                return s
            elif ls == '':
                return s + '()' + '(' + rs + ')'
            elif rs == '':
                return s + '(' + ls + ')'
            else:
                return s + '(' + ls + ')' + '(' + rs + ')'
        
        return preorder(t)