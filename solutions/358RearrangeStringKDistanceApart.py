import queue

class Solution:
    def rearrangeString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        n = len(s)
        ans = ''
        
        count = {}
        last = {}
        for c in s:
            count[c] = count.get(c, 0) + 1
            last[c] = -1
        
        q = queue.PriorityQueue()
        for key, val in count.items():
            q.put((-val, key))
        
        pos = 0
        while pos < n:
            out = set()
            v, c = q.get()
            while not q.empty() and last[c] >= 0 and pos - last[c] < k:
                out.add((v, c))
                v, c = q.get()
                
            if last[c] >= 0 and pos - last[c] < k: return ''

            for val, key in out:
                q.put((val, key))
                
            ans += c
            last[c] = pos
            count[c] -= 1
            if count[c] > 0: 
                q.put((-count[c], c))
            pos += 1
        
        return ans