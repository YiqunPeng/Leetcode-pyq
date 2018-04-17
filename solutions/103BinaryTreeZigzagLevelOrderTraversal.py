# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        
        nodes = [root]
        ans = [[root.val]]
        depth = 2
        
        while nodes:
            temp = []
            if depth % 2 == 1:
                for i in range(len(nodes)-1, -1, -1):
                    if nodes[i].left:
                        temp.append(nodes[i].left)
                    if nodes[i].right:
                        temp.append(nodes[i].right)
            else:
                for i in range(len(nodes)-1, -1, -1):
                    if nodes[i].right:
                        temp.append(nodes[i].right)
                    if nodes[i].left:
                        temp.append(nodes[i].left)
            if temp:
                ans.append([i.val for i in temp])
            nodes = temp
            depth += 1
            
        return ans
            