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
        
        def get_length(nhead):
            res = 0
            while nhead:
                res += 1
                nhead = nhead.next
            return res
        
        
        def generate_bst(n):
            if n == 0: return None          
            root = TreeNode(-1)

            root.left = generate_bst(n // 2)
                
            root.val = self.head.val
            self.head = self.head.next
            
            root.right = generate_bst(n - n // 2 - 1)
            
            return root
            

        nhead = head
        n = get_length(nhead)
        return generate_bst(n)