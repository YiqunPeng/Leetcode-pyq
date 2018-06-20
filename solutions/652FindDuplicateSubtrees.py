class Solution:
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        dic = {}
        ans = []
        
        def serialize(node):
            if not node:
                return '#'
            else:
                s = str(node.val) + ' ' + serialize(node.left) + ' ' + serialize(node.right)
                if s in dic and dic[s] == 0:
                    dic[s] = 1
                    ans.append(node)
                if s not in dic:
                    dic[s] = 0
            return s

        serialize(root)
        return ans
        