class Solution:
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        def find(edge):
            if parent[edge] != edge:
                parent[edge] = find(parent[edge])
            return parent[edge]

        
        n = len(edges)
        parent = {i: i for i in range(1, n + 1)}
        
        candidA, candidB = None, None
        for u, v in edges:
            if parent[v] == v:
                parent[v] = u
            else:
                candidB = [parent[v], v]
                candidA = [u, v]

        parent = {i: i for i in range(1, n + 1)}
        
        for u, v in edges:
            if [u, v] == candidA: continue
            
            if find(u) == find(v):
                if not candidA: return [u, v]
                return candidB
            else:
                parent[v] = parent[u]
            
        return candidA