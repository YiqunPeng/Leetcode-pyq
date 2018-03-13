class Solution:
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        def backtracking(ans, k, n, cur, cur_sum, cur_len, s, e):
            if cur_sum == n and cur_len == k:
                ans.append(copy.deepcopy(cur))
                return 0
            if cur_len > k or cur_sum > n:
                return -1
            
            for i in range(s, e):
                cur.append(i)
                res = backtracking(ans, k, n, cur, cur_sum+i, cur_len+1, i+1, e)
                cur.pop(-1)
                if res == -1 or res == 0:
                    break
        
        
        ans = []
        backtracking(ans, k, n, [], 0, 0, 1, 10)
        
        return ans