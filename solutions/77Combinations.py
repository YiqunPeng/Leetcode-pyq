class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def backtracking(ans, cur, cur_len, pos, n, k):
            if cur_len == k:
                ans.append(cur)
                return 
            
            for i in range(pos, n+1):
                backtracking(ans, cur+[i], cur_len+1, i+1, n, k)
        
        ans = []
        backtracking(ans, [], 0, 1, n, k)
        return ans