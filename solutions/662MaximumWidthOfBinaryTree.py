class Solution:
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        
        ans = 1
        nodes = [(root, 0)]
        
        while nodes:
            l_node, l_pos = nodes[0]
            r_node, r_pos = nodes[-1]        
            ans = max(ans, r_pos - l_pos + 1)
            
            n_nodes = []
            for node in nodes:
                n, p = node[0], node[1]
                if n.left:
                    n_nodes.append((n.left, p * 2))
                if n.right:
                    n_nodes.append((n.right, p * 2 + 1))  
            nodes = n_nodes
            
        return ans
