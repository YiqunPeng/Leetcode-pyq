# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def find_path(r):
            if not r.left and not r.right:
                return [0,0]
            left, right = [0,0], [0,0]
            v = r.val
            l_v, r_v = v - 1, v - 1
            if r.left:
                l_v = r.left.val
                left = find_path(r.left)
            if r.right:
                r_v = r.right.val
                right = find_path(r.right)
            if v == l_v and v == r_v:
                two_side = left[1] + right[1] + 2
                one_side = max(left[1], right[1]) + 1
                return [max(two_side, one_side, left[0], right[0]), one_side]
            elif v == l_v and v != r_v:
                return [max(left[0],right[0],left[1]+1), left[1]+1]
            elif v == r_v and v != l_v:
                return [max(left[0],right[0],right[1]+1), right[1]+1]
            else:
                return [max(left[0],right[0]),0]
            
        
        if not root: return 0
        return max(find_path(root))
        