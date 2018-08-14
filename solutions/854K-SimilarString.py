class Solution:
    def kSimilarity(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """  
        def pre_process(A, B):
            res = 0
            for i in range(len(A)):
                if A[i] == B[i]: continue
                for j in range(i+1, len(B)):
                    if A[i] == B[j] and A[j] == B[i]:
                        A[i], A[j] = A[j], A[i]
                        res += 1
                        break
            return res
        
        def dfs(A, B, start):
            if start == len(A): return 0
            if A[start] == B[start]: return dfs(A, B, start + 1)
            
            res = sys.maxsize
            for i in range(start + 1, len(A)):
                if A[i] != B[i] and A[i] == B[start]:
                    A[i], A[start] = A[start], A[i]
                    res = min(res, dfs(A, B, start + 1) + 1)
                    A[start], A[i] = A[i], A[start]
            
            return res
               
        A, B = list(A), list(B)      
        return pre_process(A, B) + dfs(A, B, 0)
    
    # bfs
    # time: O()
    # space: O()
    # def kSimilarity(self, A, B):
    #     """
    #     :type A: str
    #     :type B: str
    #     :rtype: int
    #     """
    #     def swap(s, i, j):
    #         s_list = s[:]
    #         s_list[i], s_list[j] = s_list[j], s_list[i]
    #         return s_list


    #     if A == B: return 0

    #     A, B = list(A), list(B)

    #     nodes = set()
    #     nodes.add(str(A))

    #     queue = collections.deque()
    #     queue.append((A, 0))

    #     pos = 0
    #     while queue:
    #         node, k = queue.popleft()

    #         while pos < len(B) and node[pos] == B[pos]:
    #             pos += 1

    #         for i in range(pos + 1, len(B)):
    #             if node[i] != B[i] and B[pos] == node[i]:
    #                 nxt = swap(node, i, pos)
    #                 if nxt == B: 
    #                     return k + 1
    #                 queue.append((nxt, k + 1))
    #                 nodes.add(str(nxt))

    #         pos -= 1
