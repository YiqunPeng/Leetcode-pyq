# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        neg_inf = -sys.maxsize
        pos_inf = sys.maxsize
        
        def postorder(node, max_val, lower, upper):     
            if not node: 
                return [0, max_val, lower, upper]
            if not node.left and not node.right: 
                max_val = max(max_val, 1)
                return [1, max_val, node.val, node.val]

            left = postorder(node.left, max_val, lower, upper)
            right = postorder(node.right, max_val, lower, upper)
        
            if left[0] == -1 or right[0] == -1:
                max_val = max(max_val, left[1], right[1])
                return [-1, max_val, pos_inf, neg_inf]
            
            res = 1
            if (not node.right or right[2] > node.val) and (not node.left or left[3] < node.val):
                res += left[0] + right[0]
            else:
                res = -1
                
            return [res, max(res, left[1], right[1], max_val), min(lower, left[2], node.val), max(upper, right[3], node.val)]
   
        return postorder(root, 0, pos_inf, neg_inf)[1]