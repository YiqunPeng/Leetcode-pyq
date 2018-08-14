# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # iterative inorder traverse
    # time: O(n)
    # space: O(n)
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans = sys.maxsize
        pre = sys.maxsize
        stack = []
        
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                if pre != sys.maxsize:
                    ans = min(ans, abs(pre - root.val))
                    pre = root.val
                else:
                    pre = root.val
                root = root.right
        
        return ans