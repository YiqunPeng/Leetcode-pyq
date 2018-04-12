class Solution:
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        N = len(graph)
        path, ans = [], []
        
        for node in graph[0]:
            if node == N - 1:
                ans.append([0, node])
            else:
                path.append([0, node])
        
        while path:
            p = path[0]
            for i in graph[p[-1]]:
                if i == N - 1:
                    ans.append(p + [i])
                else:
                    path.append(p + [i])
            path.pop(0)
        
        return ans