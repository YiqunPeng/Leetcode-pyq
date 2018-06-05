class Solution:
    def numBusesToDestination(self, routes, S, T):
        """
        :type routes: List[List[int]]
        :type S: int
        :type T: int
        :rtype: int
        """
        if S == T: return 0
        
        v = [False] * len(routes)
        
        s2r = {}
        for i in range(len(routes)):
            for s in routes[i]:
                if s not in s2r:
                    s2r[s] = [i]
                else:
                    s2r[s].append(i)
        
        q = []
        for i in range(len(routes)):
            if S in routes[i] and not v[i]:
                v[i] = True
                for s in routes[i]:
                    q.append((s, 1))
        
        while q:
            s, d = q.pop(0)
            if s == T:
                return d
            for r in s2r[s]:
                if not v[r]:
                    v[r] = True
                    for ss in routes[r]:
                        q.append((ss, d+1))
        
        return -1