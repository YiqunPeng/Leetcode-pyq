class Solution:
    def maxVacationDays(self, flights, days):
        """
        :type flights: List[List[int]]
        :type days: List[List[int]]
        :rtype: int
        """
        n, k = len(days), len(days[0])
        
        dp = [[-1] * n for i in range(k)]
        dp[0][0] = days[0][0]
        
        flights_dict = collections.defaultdict(set)
        for i in range(n):
            for j in range(n):
                if flights[i][j] == 1:
                    flights_dict[j].add(i)
        
        for key in flights_dict:
            if 0 in flights_dict[key]:
                dp[0][key] = days[key][0]
        
        for i in range(1, k):
            for j in range(n):
                if dp[i-1][j] != -1:
                    dp[i][j] = dp[i-1][j]
                for pre_j in flights_dict[j]:
                    if dp[i-1][pre_j] != -1: 
                        dp[i][j] = max(dp[i-1][pre_j], dp[i][j])
                if dp[i][j] != -1: dp[i][j] += days[j][i]
        
        return max(dp[-1])