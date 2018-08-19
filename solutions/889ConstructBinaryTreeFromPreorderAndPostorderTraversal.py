# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """        
        if not pre: return None
        if len(pre) == 1: return TreeNode(pre[0])
        
        root = TreeNode(pre[0])
        
        r_s = pre.index(post[-2])
        if r_s == 1:
            root.left = None
            root.right = self.constructFromPrePost(pre[1:], post[:-1])
        else:
            l_e = post.index(pre[1])
            root.left = self.constructFromPrePost(pre[1:r_s], post[:l_e+1])
            root.right = self.constructFromPrePost(pre[r_s:], post[l_e+1:-1])          

        return root