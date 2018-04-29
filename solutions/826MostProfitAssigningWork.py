class Solution:
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        d, p, w = difficulty, profit, worker
        ans = 0
        
        dic = {}
        for i in range(len(d)):
            if d[i] not in dic:
                dic[d[i]] = p[i]
            else:
                if dic[d[i]] < p[i]:
                    dic[d[i]] = p[i]
        
        dic = sorted(dic.items(), key=lambda x:x[0])
        
        w.sort()
            
        pos = 0
        max_p = 0
        flag = False
        while pos < len(dic) and dic[pos][0] <= w[0]:
            flag = True
            if dic[pos][1] > dic[max_p][1]:
                max_p = pos
            pos += 1
        
        if flag:
            ans += dic[max_p][1]
        
        for i in range(1, len(w)):
            while pos < len(dic) and dic[pos][0] <= w[i]:
                flag = True
                if dic[pos][1] > dic[max_p][1]:
                    max_p = pos
                pos += 1
            if flag:
                ans += dic[max_p][1]
        
        return ans
            
        