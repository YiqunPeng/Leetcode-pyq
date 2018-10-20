class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def backtracking(candid, curr, curr_sum):
            if curr_sum == target:
                ans.append(curr)
                return
            
            for i in range(len(candid)):
                if curr_sum + candid[i] <= target:
                    backtracking(candid[i:], curr + [candid[i]], curr_sum + candid[i])
                else:
                    break
        
        
        candidates.sort()
        
        ans = []
        backtracking(candidates, [], 0)
        return ans