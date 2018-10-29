class Solution:
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if not edges: return [0]
        
        graph = collections.defaultdict(set)
        for e in edges:
            graph[e[0]].add(e[1])
            graph[e[1]].add(e[0])
            
        curr = []
        for v in graph:
            if len(graph[v]) == 1:
                curr.append(v)
        
        while 1:
            nxt = []
            
            for node in curr:
                for neighbor in graph[node]:
                    graph[neighbor].remove(node)
                    if len(graph[neighbor]) == 1: nxt.append(neighbor)
                del graph[node]

            if not nxt: return curr
            curr = nxt