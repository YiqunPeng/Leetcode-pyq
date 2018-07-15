import queue

class Solution:
    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        dic = {}
        a_dic = {}
        
        a = queue.PriorityQueue()
        for i in A:
            a.put(i)
            a_dic[i] = a_dic.get(i, 0) + 1
        b = queue.PriorityQueue()
        for i in B:
            b.put(i)
            
        while not a.empty() and not b.empty():
            b_v = b.get()
            a_v = a.get()
            while not a.empty() and a_v <= b_v:
                a_v = a.get()
            if a_v > b_v: 
                if b_v not in dic:
                    dic[b_v] = [a_v]
                else:
                    dic[b_v].append(a_v)
                a_dic[a_v] -= 1
        
        unused = []
        for key in a_dic:
            if a_dic[key] > 0:
                unused = unused + [key] * a_dic[key]
        pos = 0
                
        ans = [0] * len(A)
        for i in range(len(ans)):
            if B[i] in dic:
                ans[i] = dic[B[i]][-1]
                dic[B[i]].pop()
                if not dic[B[i]]:
                    del dic[B[i]]
            else:
                ans[i] = unused[pos]
                pos += 1
        return ans
        

        
        
        