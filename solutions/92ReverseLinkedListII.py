class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        loop = n - m + 1
        
        if loop == 1: return head
        
        o_head = head
        
        cnt = 1
        be = o_head
        while cnt < m - 1:
            be = be.next
            cnt += 1

        if m != 1:
            pre = be.next
            fi = pre.next
            o_fi = pre
        else:
            pre = o_head
            fi = pre.next
            o_fi = o_head
        
        n_head = None
        af = None
        
        for i in range(1, loop):
            curr = fi
            if i == loop - 1 and curr:
                af = curr.next
            if fi: 
                fi = fi.next
            if curr: 
                curr.next = pre
            pre = curr

        if m != 1:
            be.next = pre
            o_fi.next = af
            return o_head
        else:
            n_head = pre
            o_fi.next = af
            return n_head
        