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
    # inorder traversal
    # time: O(n)
    # space: O(1)
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        self.head = head
        
        def generate(length):
            if length == 0: return None
            
            node = TreeNode(0)
            node.left = generate(length // 2)
            
            node.val = self.head.val
            self.head = self.head.next
            
            node.right = generate(length - length // 2 - 1)
            
            return node
            

        n_head = head
        
        length = 0
        while n_head:
            length += 1
            n_head = n_head.next
            
        return generate(length)