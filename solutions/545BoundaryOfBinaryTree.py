# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        left, leaves, right = [], [], []        
        
        def find_left_boundary(node):
            if not node: return
            left.append(node)
            if node.left:
                find_left_boundary(node.left)
            elif node.right and node != root:
                find_left_boundary(node.right)
        
        def find_right_boundary(node):
            if not node: return
            right.append(node)
            if node.right:
                find_right_boundary(node.right)
            elif node.left and node != root:
                find_right_boundary(node.left)
                
        def find_leaves(node):
            if not node: return 
            if not node.left and not node.right:
                leaves.append(node)
            if node.left:
                find_leaves(node.left)
            if node.right:
                find_leaves(node.right)
                  
        if not root: return []
        
        ans = [root.val]
        
        find_left_boundary(root)
        find_leaves(root)
        find_right_boundary(root)

        nodes = left + leaves + right[::-1]     
        node_set = set()
        node_set.add(str(root))
        for node in nodes:
            if str(node) not in node_set:
                node_set.add(str(node))
                ans.append(node.val)
        
        return ans
        
        