class Solution:  
    # bfs
    def shortestPathLength(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        state = set()
        queue = collections.deque()

        n = len(graph)
        for i in range(n):
            v = 1 << i
            state.add((v, i))
            queue.append((v, i, 0))

        while queue:
            v, node, cost = queue.popleft()
            if v == (1 << n) - 1: 
                return cost
            neighbors = graph[node]
            for nei in neighbors:
                nv = v | (1 << nei)
                if (nv, nei) not in state:
                    queue.append((nv, nei, cost + 1))
                    state.add((nv, nei))

        return -1