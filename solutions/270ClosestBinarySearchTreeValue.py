# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # inorder traversal, iterative
    # time: O(n)
    # space: O(n)
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        ans = -1
        diff = sys.maxsize
        
        stack = []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                if diff > abs(target - root.val):
                    diff = abs(target - root.val)
                    ans = root.val
                elif diff < abs(target - root.val):
                    return ans
                root = root.right
        
        return ans 