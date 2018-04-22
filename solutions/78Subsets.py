class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtracking(ans, s_set, r_nums, s_len, t_len):
            if s_len == t_len:
                ans.append(s_set)
                return
            for i in range(len(r_nums)):
                backtracking(ans, s_set+[r_nums[i]], r_nums[i+1:], s_len+1, t_len)
            
        
        ans = [[]]
        
        for i in range(1, len(nums)+1):
            backtracking(ans, [], nums, 0, i)
            
        return ans
        