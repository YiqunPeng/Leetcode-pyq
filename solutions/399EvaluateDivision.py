class Solution:
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        def bfs(q):
            queue = collections.deque()
            queue.append((q[0], 1.0))
            visited = set()
            while queue:
                s, v = queue.popleft()
                if s == q[1]:
                    return v
                for nxt in adj[s]:
                    if nxt not in visited:
                        queue.append((nxt, v * val[(s, nxt)]))
                        visited.add(nxt) 
            return -1.0
        
        adj = collections.defaultdict(list)
        val = collections.defaultdict(float)
        
        for i, e in enumerate(equations):
            val[(e[0], e[1])] = values[i]
            val[(e[1], e[0])] = 1.0 / values[i]
            adj[e[0]].append(e[1])
            adj[e[1]].append(e[0])
        
        ans = []
        for q in queries:
            if q[0] not in adj or q[1] not in adj:
                ans.append(-1.0)
                continue
            ans.append(bfs(q))
    
        return ans  