class Solution:
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs: return 0
        
        n, k = len(costs), len(costs[0])     
        f_min, s_min = sys.maxsize, sys.maxsize
        f_min_p = -1
        
        dp = [0 for i in range(k)]
        for i in range(k):
            dp[i] = costs[0][i]
            if f_min > dp[i]:
                s_min = f_min
                f_min = dp[i]
                f_min_p = i
            elif s_min > dp[i]:
                s_min = dp[i]
            
        for i in range(1, n):
            t_f_min, t_s_min = sys.maxsize, sys.maxsize
            t_f_min_p = -1
            for p in range(k):
                if p != f_min_p:
                    dp[p] = f_min + costs[i][p]
                else:
                    dp[p] = s_min + costs[i][p]
                if t_f_min > dp[p]:
                    t_s_min = t_f_min
                    t_f_min = dp[p]
                    t_f_min_p = p
                elif t_s_min > dp[p]:
                    t_s_min = dp[p]
            f_min, s_min, f_min_p = t_f_min, t_s_min, t_f_min_p   
                
        return min(dp)
        
