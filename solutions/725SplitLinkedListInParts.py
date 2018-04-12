# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        ans = []
        n = 0
        head = root
        while head:
            n += 1
            head = head.next
        (div, mod) = divmod(n, k)
        
        for i in range(1, k+1):
            if i <= mod:
                cnt = div + 1
            else:
                cnt = div
            part = []
            for j in range(cnt):
                part.append(root.val)
                root = root.next
            ans.append(part)
            
        return ans
            