class Solution:
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """     
        father = [i for i in range(len(edges)+1)]
        rank = [1 for i in range(len(edges)+1)]
        
        def find(v):
            if father[v] == v:
                return v
            else:
                father[v] = find(father[v])
                return father[v]
        
        def unite(v1, v2):
            f_v1, f_v2 = find(v1), find(v2)
            if f_v1 == f_v2:
                return
            if rank[v1] >= rank[v2]:
                father[f_v2] = f_v1
                if rank[v1] == rank[v2]: rank[v1] += 1
            else:
                father[f_v1] = f_v2

        for edge in edges:
            if find(edge[0]) == find(edge[1]):
                return edge
            unite(edge[0], edge[1])
            