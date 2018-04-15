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
        table = [-1] * 10000
        for g in G:
            table[g] = 1
            
        ans = 0
        flag = 0
        
        while head:
            if table[head.val] == 1:
                flag = 1
            elif table[head.val] == -1:
                ans += flag
                flag = 0
            head = head.next
        
        return ans + flag
            
        