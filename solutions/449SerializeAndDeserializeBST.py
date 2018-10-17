# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """
        Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        preorder = []
        stack = []
        while root or stack:
            if root:
                preorder.append(str(root.val))
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()     
                root = root.right

        return ' '.join(preorder)
        

    def deserialize(self, data):
        """
        Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        def build(preorder, inorder):
            if not preorder:
                return None
            
            rval = preorder[0]
            idx = inorder.index(rval)
            
            root = TreeNode(rval)
            root.left = build(preorder[1:idx+1], inorder[:idx])
            root.right = build(preorder[idx+1:], inorder[idx+1:])
            
            return root
        
        if not data: return None
        preorder = map(int, data.split(' '))
        inorder = sorted(preorder)
        
        return build(preorder, inorder)
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))