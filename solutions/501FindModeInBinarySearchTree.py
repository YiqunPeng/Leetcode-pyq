# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def handle(val, cur_val, cur_cnt, max_cnt, a):
            # print(val)
            # print(cur_val)
            # print(a)
            if val != cur_val:
                cur_val = val
                cur_cnt = 1
            else:
                cur_cnt += 1
            if cur_cnt > max_cnt:
                max_cnt = cur_cnt
                a = []
                a.append(cur_val)
            elif cur_cnt == max_cnt:
                a.append(cur_val)
            # print(a)
            return cur_val, cur_cnt, max_cnt, a
        
        
        def inorder(root, cur_val, cur_cnt, max_cnt, a):
            if root.left: 
                cur_val, cur_cnt, max_cnt, a = inorder(root.left, cur_val, cur_cnt, max_cnt, a)
            cur_val, cur_cnt, max_cnt, a = handle(root.val, cur_val, cur_cnt, max_cnt, a)
            if root.right:
                cur_val, cur_cnt, max_cnt, a = inorder(root.right, cur_val, cur_cnt, max_cnt, a)
            return cur_val, cur_cnt, max_cnt, a
        
        
        ans = []
        if not root: return ans
        
        return(inorder(root, root.val, 0, 0, ans)[-1])
        