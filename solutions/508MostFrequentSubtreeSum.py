# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        dic = {}
        
        def subtree_sum(node):
            if not node.left and not node.right:
                dic[node.val] = dic.get(node.val, 0) + 1
                return node.val
            left, right = 0, 0
            if node.left:
                left = subtree_sum(node.left)
            if node.right:
                right = subtree_sum(node.right)
            sum_v = node.val + left + right
            dic[sum_v] = dic.get(sum_v, 0) + 1
            return sum_v
        
        
        if not root: return []
        subtree_sum(root)
        ans = []
        max_v = max(dic.values())
        for key in dic.keys():
            if dic[key] == max_v:
                ans.append(key)
        return ans