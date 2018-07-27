# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        G = set(G)
        ans = len(G)
        
        while head:
            while head.val in G and head.next and head.next.val in G:
                head = head.next
                ans -= 1
            head = head.next
            
        return ans