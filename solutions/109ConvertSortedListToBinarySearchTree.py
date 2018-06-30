# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def find_mid(self, head, tail):
        if not head: return None
        if head == tail: return None
        f, s = head, head
        while f.next and f.next != tail and f.next.next != tail:
            f = f.next.next
            s = s.next
        return s
        
    def construct_tree(self, l_mid, l_head, l_tail):
        if not l_mid: return None
        root = TreeNode(l_mid.val)
        root.left = self.construct_tree(self.find_mid(l_head, l_mid), l_head, l_mid)
        root.right = self.construct_tree(self.find_mid(l_mid.next, l_tail), l_mid.next, l_tail)
        return root
    
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        return self.construct_tree(self.find_mid(head, None), head, None)
    
        
