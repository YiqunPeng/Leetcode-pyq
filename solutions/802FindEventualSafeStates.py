class Solution:
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        nodes = [0] * len(graph)
        
        def dfs(node):
            nodes[node] = 1
            for nxt in graph[node]:
                if nodes[nxt] == 1 or (nodes[nxt] == 0 and dfs(nxt)):
                    return True
            nodes[node] = 2
            return False
        
        for i in range(len(graph)):
            if not nodes[i]:
                dfs(i)
        
        return [i for i in range(len(nodes)) if nodes[i] == 2]
