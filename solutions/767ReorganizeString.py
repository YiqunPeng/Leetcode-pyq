class Solution:
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        dic = {}
        for c in S:
            dic[c] = dic.get(c, 0) - 1
        
        pq = [(val, key) for key, val in dic.items()]
        heapq.heapify(pq)
         
        pre_cnt, pre = heapq.heappop(pq)
        pre_cnt += 1
        ans = pre
        while pq:
            curr_cnt, curr = heapq.heappop(pq)
            curr_cnt += 1
            ans = ans + curr
            if pre_cnt <= -1:
                heapq.heappush(pq, (pre_cnt, pre))
            pre_cnt = curr_cnt
            pre = curr
                
        return ans if len(ans) == len(S) else ''
            
        
        
        