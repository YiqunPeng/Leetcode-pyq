# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        dq = collections.deque()
        stack = []
        
        while root or stack:
            if root:
                dq.appendleft(root.val)
                stack.append(root)
                root = root.right
            else:
                root = stack.pop()
                root = root.left
        
        return [i for i in dq]        