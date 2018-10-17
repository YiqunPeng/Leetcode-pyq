# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # recursive
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        
        if root.left and root.right:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
        else:
            return max(self.minDepth(root.left), self.minDepth(root.right)) + 1


    # iterative
    # def minDepth(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: int
    #     """
    #     if not root: return 0
        
    #     q = collections.deque([(root, 1)])
    #     while q:
    #         node, depth = q.popleft()
    #         if not node.left and not node.right:
    #             return depth
    #         if node.left:
    #             q.append((node.left, depth+1))
    #         if node.right:
    #             q.append((node.right, depth+1))
         
