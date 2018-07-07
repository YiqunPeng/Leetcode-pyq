# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def subtree(a):
            res = []
            if not a: return []
            if len(a) == 1: return [TreeNode(a[0])]
            if len(a) == 2:
                n1 = TreeNode(a[1])
                n1.left = TreeNode(a[0])
                n2 = TreeNode(a[0])
                n2.right = TreeNode(a[1])
                return [n1, n2]
            for i in range(len(a)):
                left = subtree(a[:i])
                right = subtree(a[i+1:])
                if not left:
                    for r in right:
                        root = TreeNode(a[i])
                        root.right = r
                        res.append(root)
                elif not right:
                    for l in left:
                        root = TreeNode(a[i])
                        root.left = l
                        res.append(root)
                else:
                    for l in left:
                        for r in right:
                            root = TreeNode(a[i])
                            root.left = l
                            root.right = r
                            res.append(root)
            return res

        return subtree(range(1, n+1))
