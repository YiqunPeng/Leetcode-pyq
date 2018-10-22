class Solution:
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if len(num) == k: return '0'
        
        queue = collections.deque()
        for n in num:
            n = int(n)
            while queue and queue[-1] > n and k:
                queue.pop()
                k -= 1
            queue.append(n)
        
        while k:
            queue.pop()
            k -= 1

        while len(queue) > 1 and queue[0] == 0: queue.popleft()
            
        ans = ''.join(map(str, queue))
        return ans