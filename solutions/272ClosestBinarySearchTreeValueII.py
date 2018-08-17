# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # two stacks
    # time: O(logn) in best case
    # space: O(n)
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        def get_prev():
            res = prev.pop()
            if res.left:
                prev.append(res.left)
                while prev[-1].right:
                    prev.append(prev[-1].right)
            return res.val
        
        def get_succ():
            res = succ.pop()
            if res.right:
                succ.append(res.right)
                while succ[-1].left:
                    succ.append(succ[-1].left)
            return res.val
            
        
        ans = []
        old_root = root
        
        prev, succ = [], []
        while root:
            if root.val <= target:
                prev.append(root)
                root = root.right
            else:
                succ.append(root)
                root = root.left

        for i in range(k):
            if not succ and prev:
                ans.append(get_prev())
            elif not prev and succ:
                ans.append(get_succ())
            else:
                prev_d = target - prev[-1].val
                succ_d = succ[-1].val - target
                if prev_d < succ_d:
                    ans.append(get_prev())
                else:
                    ans.append(get_succ())
        
        return ans
        
    
    # inorder traversal, double-ended queue
    # time: O(n)
    # space: O(n)
    # def closestKValues(self, root, target, k):
    #     """
    #     :type root: TreeNode
    #     :type target: float
    #     :type k: int
    #     :rtype: List[int]
    #     """
    #     queue = collections.deque([])

    #     stack = []
    #     while stack or root:
    #         if root:
    #             stack.append(root)
    #             root = root.left
    #         else:
    #             root = stack.pop()
    #             if len(queue) < k:
    #                 queue.append(root.val)
    #             else:
    #                 if abs(queue[0]-target) > abs(root.val-target):
    #                     queue.popleft()
    #                     queue.append(root.val)
    #                 else:
    #                     return [i for i in queue]
    #             root = root.right

    #     return [i for i in queue]
