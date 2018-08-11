class Solution:
    def numBusesToDestination(self, routes, S, T):
        """
        :type routes: List[List[int]]
        :type S: int
        :type T: int
        :rtype: int
        """
        if S == T: return 0
        
        v = set()
        
        s2r = collections.defaultdict(list)
        for i in range(len(routes)):
            for s in routes[i]:
                s2r[s].append(i)
        
        q = collections.deque()
        for i in range(len(routes)):
            if S in routes[i] and i not in v:
                v.add(i)
                for s in routes[i]:
                    q.append((s, 1))
        
        while q:
            s, d = q.popleft()
            if s == T:
                return d
            for r in s2r[s]:
                if r not in v:
                    v.add(r)
                    for ss in routes[r]:
                        q.append((ss, d+1))
        
        return -1