from queue import Queue

class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        indegree = [0] * numCourses
        adj = [[] for i in range(numCourses)]
        
        for pre in prerequisites:
            adj[pre[1]].append(pre[0])
            indegree[pre[0]] += 1

        cnt = 0
        
        q = Queue()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.put(i)
                cnt += 1

        while not q.empty():
            v = q.get()
            for w in adj[v]:
                indegree[w] -= 1
                if indegree[w] == 0:
                    q.put(w)
                    cnt += 1
                    
        return True if cnt == numCourses else False
            
        
        