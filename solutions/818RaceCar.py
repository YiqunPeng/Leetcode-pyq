class Solution:
    def racecar(self, target):
        """
        :type target: int
        :rtype: int
        """
        q = collections.deque()
        q.append((0, 1, 0))
        
        v = set([(0, 1)])
        
        while q:
            p, s, m = q.popleft()
 
            # A
            np = p + s
            ns = s * 2   
            if np == target: return m + 1
            
            if (np, ns) not in v and (-20000 <= np <= 20000):
                q.append((np, ns, m + 1))
                v.add((np, ns))
            
            # R
            np = p
            ns = 1 if s <= 0 else -1
            if np == target: return m + 1
            
            if (np, ns) not in v and (-20000 <= np <= 20000):
                q.append((np, ns, m + 1))
                v.add((np, ns))
        
        return -1