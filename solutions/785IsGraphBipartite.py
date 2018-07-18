import queue

class Solution:
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        subsets = [set(), set()]
        visited = set()

        for i in range(len(graph)):
            if not graph[i]:
                visited.add(i)
                continue
            if i in visited:
                continue
            q = queue.Queue()
            q.put((i, 0))
            while not q.empty():
                node, sub = q.get()
                neighbors = graph[node]
                for n in neighbors:
                    if n in subsets[sub]:
                        return False
                    else:
                        if n not in visited:
                            q.put((n, 1 - sub))
                            subsets[1-sub].add(n)
                            visited.add(n)
        
        return True