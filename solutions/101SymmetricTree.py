# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # recursive, dfs
    # time: O(n)
    # space: O(n)
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # dfs, recursive
        def is_symm_sub(r1, r2):
            if not r1 and not r2: return True
            if not r1 or not r2: return False
            if r1.val != r2.val: return False
            
            return is_symm_sub(r1.left, r2.right) and is_symm_sub(r2.left, r1.right)

        if not root: return True
        return is_symm_sub(root.left, root.right)
    

    # level traverse, bfs, iterative
    # time: O(n)
    # space: O(n)
    # def isSymmetric(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: bool
    #     """
    #     if not root: return True
    #     if not root.left and not root.right: return True
    #     if not (root.left and root.right): return False

    #     queue = [(root.left, 0), (root.right, 1)]

    #     level = 1
    #     while queue:
    #         nxt = collections.deque()
    #         l, r = len(queue) // 2 - 1, len(queue) // 2
    #         while l >= 0:
    #             ln, lp = queue[l][0], queue[l][1]
    #             rn, rp = queue[r][0], queue[r][1]

    #             if lp + rp != 2 ** level - 1: return False
    #             if ln.val != rn.val: return False

    #             if ln.right:
    #                 nxt.appendleft((ln.right, lp * 2 + 1))
    #             if ln.left:
    #                 nxt.appendleft((ln.left, lp * 2))
    #             if rn.left:
    #                 nxt.append((rn.left, rp * 2))
    #             if rn.right:
    #                 nxt.append((rn.right, rp * 2 + 1))

    #             l, r = l - 1, r + 1

    #         if len(nxt) % 2 != 0: return False    

    #         queue = nxt
    #         level += 1

    #     return True



