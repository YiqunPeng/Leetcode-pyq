# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root: return ''

        q = [(root, 0)]
        res = str(root.val) + ',0'
        while q:
            node, pos = q.pop(0)
            if node.left:
                q.append((node.left, pos*2+1))
                res = res + '#' + str(node.left.val) + ',' + str(pos*2+1)
            if node.right:
                q.append((node.right, pos*2+2))
                res = res + '#' + str(node.right.val) + ',' + str(pos*2+2)

        return res


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data: return None
        
        nodes = data.split('#')
        
        node_pos = {}
        
        r = nodes[0].split(',')
        root = TreeNode(int(r[0]))
        node_pos[int(r[1])] = root
        
        for i in range(1, len(nodes)):
            n = nodes[i].split(',')
            val, pos = int(n[0]), int(n[1])
            node = TreeNode(val)
            node_pos[pos] = node
            if pos % 2 == 0:
                node_pos[(pos-1)//2].right = node
            else:
                node_pos[(pos-1)//2].left = node
        
        return root
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))