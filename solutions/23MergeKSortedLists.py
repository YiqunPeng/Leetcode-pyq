# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        def merge_two_lists(l1, l2):
            if not l1 and not l2: return None
            if not l1: return l2
            if not l2: return l1
            if l1.val < l2.val:
                if l1.next:
                    l1.next = merge_two_lists(l1.next, l2)
                else:
                    l1.next = l2
                return l1
            else:
                if l2.next:
                    l2.next = merge_two_lists(l1, l2.next)
                else:
                    l2.next = l1
                return l2
        
        
        while len(lists) > 1:
            l1, l2 = lists.pop(0), lists.pop(0)
            lists.append(merge_two_lists(l1, l2))
            
        return lists[0] if lists else []