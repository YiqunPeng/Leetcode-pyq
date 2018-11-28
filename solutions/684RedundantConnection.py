class Solution:
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]
        
        
        def union(node1, node2):
            p1, p2 = find(node1), find(node2)
            if p1 != p2: parent[p2] = p1
                
        
        n = len(edges)
        parent = {i: i for i in range(1, n + 1)}
        
        for s, e in edges:
            if find(s) == find(e): return [s, e]
            union(s, e)