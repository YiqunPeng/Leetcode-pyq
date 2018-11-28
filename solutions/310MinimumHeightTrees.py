class Solution:
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 0: return []
        if n == 1: return [0]
        
        graph = collections.defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
            
        curr = []
        for key, val in graph.items():
            if len(val) == 1: curr.append(key)
                
        while True:
            nxt = []
            
            for node in curr:
                for neighbor in graph[node]:
                    graph[neighbor].remove(node)
                    if len(graph[neighbor]) == 1: nxt.append(neighbor)
                del graph[node]
                    
            if not nxt: return curr
            curr = nxt