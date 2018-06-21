class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()    
        ans = [[]]
        
        def backtracking(subset, nums_len, pos):
            if len(subset) == nums_len:
                return
            
            for i in range(pos, nums_len):
                if i == pos or (i > pos and nums[i] != nums[i-1]):
                    ans.append(subset + [nums[i]])
                    backtracking(subset + [nums[i]], nums_len, i + 1)
            
        
        backtracking([], len(nums), 0)
        return ans