class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def backtracking(ans, candi, tar, cur, cur_sum, s, e):
            if cur_sum == tar:
                ans.append(copy.deepcopy(cur))
                return 0 
            if cur_sum > tar:
                return -1
            
            for i in range(s, e):
                cur.append(candi[i])                
                res = backtracking(ans, candi, tar, cur, cur_sum+candi[i], i, e)
                cur.pop(-1)
                if res == -1 or res == 0:
                    break
        
        
        candidates = list(set(candidates))
        candidates.sort()
                
        ans = []      
        backtracking(ans, candidates, target, [], 0, 0, len(candidates))
        
        return ans
        