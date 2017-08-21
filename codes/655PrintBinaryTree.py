# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        layers = self.bfs(root)
        height = len(layers)
        ans = [['']*(2**height-1) for i in xrange(height)]
        postions = [i for i in xrange(0, 2**height-1, 2)]
        for i in xrange(height-1, -1, -1):
            for j in xrange(0, len(postions)):
                if layers[i][j]:
                    ans[i][postions[j]] = str(layers[i][j].val)
            new_pos = [(postions[i]+postions[i+1])/2 for i in xrange(0, len(postions)-1, 2)]
            postions = new_pos
        return ans
            
    
    def bfs(self, root):
        layers = [[root]]
        next_layer = layers[-1]
        while next_layer:
            nodes = []
            for node in next_layer:
                if not node:
                    nodes.append(None)
                    nodes.append(None)
                    continue
                if node.left: 
                    nodes.append(node.left)
                else:
                    nodes.append(None)
                if node.right:
                    nodes.append(node.right)
                else:
                    nodes.append(None)
            flag = 0
            for node in nodes:
                if node:
                    flag = 1
                    break
            if flag:
                layers.append(nodes)
                next_layer = layers[-1]
            else:
                next_layer = []
        return layers
                        
            
                
        
        