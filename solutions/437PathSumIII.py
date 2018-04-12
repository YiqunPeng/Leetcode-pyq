# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """    
        def dfs(r, sum):
            cnt = 0
            left, right, cur = [[],0], [[],0], []
            val = 0
            if r.left:
                left = dfs(r.left, sum)
            if r.right:
                right = dfs(r.right, sum)
            for i in left[0]+right[0]+[0]:
                val = r.val + i
                cur.append(val)
                if val == sum:
                    cnt += 1
            return [cur, cnt+left[1]+right[1]]
    
        if not root: return 0
        
        ans = dfs(root, sum)
        
        return ans[1]
        