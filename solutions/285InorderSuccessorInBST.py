# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        ans = None
        
        def search(node, f):
            if node.val == p.val:
                if node.right:
                    return search(node.right, f)
                else:
                    if not f:
                        ans = None
                    else:
                        ans = f
                return ans
            elif node.val > p.val:
                if node.left:
                    return search(node.left, node)
                else:
                    ans = node
                    return ans
            else:
                if node.right:
                    return search(node.right, f)
                else:
                    ans = None
                    return ans

                
        if not root: return None
        
        ans = search(root, None)
        
        if ans:
            return ans.val
        else:
            return None
        