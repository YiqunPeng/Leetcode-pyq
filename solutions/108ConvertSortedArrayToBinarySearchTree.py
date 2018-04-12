# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def to_BST(nums, l, r):
            if l == r: return TreeNode(nums[l])
            mid = (l + r + 1) // 2
            val = nums[mid]
            node = TreeNode(val)
            if l <= mid-1:
                node.left = to_BST(nums, l, mid-1)
            if mid+1 <= r:
                node.right = to_BST(nums, mid+1, r)
            return node
        
        
        if not nums: return None
        
        return to_BST(nums, 0, len(nums)-1)