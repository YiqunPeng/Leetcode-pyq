class Solution:
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        father = [i for i in range(n)]
        size = [1 for i in range(n)]
        

        def find(node):
            if father[node] != node:
                father[node] = find(father[node])
            return father[node]
        
        
        def union(n1, n2):
            f_n1, f_n2 = find(n1), find(n2)
            if f_n1 != f_n2:
                if size[f_n1] > size[f_n2]:
                    father[f_n2] = f_n1
                    size[f_n1] += size[f_n2]
                else:
                    father[f_n1] = f_n2
                    size[f_n2] += size[f_n1]
        
        
        for e in edges:
            if find(e[0]) == find(e[1]):
                continue
            else:
                union(e[0], e[1])
        
        ans = 0
        for i in range(n):
            if father[i] == i:
                ans += 1
        return ans
                
        