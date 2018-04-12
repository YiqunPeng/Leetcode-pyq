# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        ans = []
        
        self.dfs(root)
        dic = {}
        self.traversal(root, dic)
        dic = sorted(dic.items(), key=lambda item:item[1], reverse=True)
        max = dic[0][1]
        for key, value in dic:
            if value == max:
                ans.append(int(key))
        
        return ans
    
    def dfs(self, root):
        if not root.left and not root.right:
            return root.val
        root.val = root.val + (self.dfs(root.left) if root.left else 0) + (self.dfs(root.right) if root.right else 0)
        return root.val
    
    def traversal(self, root, dic):
        if root.left: self.traversal(root.left, dic)
        if root.right: self.traversal(root.right, dic)
        dic[str(root.val)] = dic.get(str(root.val), 0) + 1