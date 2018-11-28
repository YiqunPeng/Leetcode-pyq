# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # recursive, post-order traversal
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def deep(node):
            if not node: return 0, None         
            l, r = deep(node.left), deep(node.right)
            if l[0] == r[0]:
                return l[0] + 1, node
            elif l[0] < r[0]:
                return r[0] + 1, r[1]
            else:
                return l[0] + 1, l[1]

        return deep(root)[1]
    
    
    # hash map
    # def subtreeWithAllDeepest(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: TreeNode
    #     """
    #     if not root: return None

    #     parent = {}

    #     level = [root]
    #     while True:
    #         nxt = []     
    #         for node in level:
    #             if node.left:
    #                 parent[node.left] = node
    #                 nxt.append(node.left)
    #             if node.right:
    #                 parent[node.right] = node
    #                 nxt.append(node.right)      
    #         if not nxt: break
    #         level = nxt

    #     while len(level) != 1:
    #         parents = set()          
    #         for node in level:
    #             parents.add(parent[node])
    #         level = parents

    #     return level[0]