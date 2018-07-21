class Solution:
    # Topological sort 
    # time: build graph: O(k) k -- total characters in words
    #       topo sort:   O(e + v) e -- number of edges; v -- number of vertices
    # space: store graph: O(v^2)
    #        topo sort: O(v)
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        dic = collections.defaultdict(set)
        indegree = {}
        
        for word in words:
            for c in word:
                indegree[c] = 0

        if len(words) == 1: return words[0]
        for i in range(len(words)-1):
            s1, s2 = words[i], words[i+1]
            ptr = 0
            while ptr < len(s1) and ptr < len(s2) and s1[ptr] == s2[ptr]:
                ptr += 1
            if ptr < len(s1) and ptr < len(s2) and s2[ptr] not in dic[s1[ptr]]:
                indegree[s2[ptr]] += 1
                dic[s1[ptr]].add(s2[ptr])
                
        ans = ''    
        q = collections.deque()
        for key in indegree.keys():
            if indegree[key] == 0:
                q.append(key)    
        while q:
            k = q.popleft()
            ans += k
            for v in dic[k]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)

        for v in indegree.values():
            if v > 0: return ''
        return ans
        