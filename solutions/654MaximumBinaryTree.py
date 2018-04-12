# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.construct_tree(nums, 0, len(nums)-1)
    
    def construct_tree(self, nums, l, r):
        if l > r: return None
        
        max = nums[l]
        max_pos = l
        for i in xrange(l+1, r+1):
            if nums[i] > max:
                max = nums[i]
                max_pos = i
        
        root = TreeNode(max)
        root.left = self.construct_tree(nums, l, max_pos-1)
        root.right = self.construct_tree(nums, max_pos+1, r)
        
        return root