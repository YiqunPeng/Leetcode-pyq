class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtracking(ans, cur, cur_len, nums, nums_len):
            if cur_len == nums_len:
                ans.append(cur)
                return 
            
            for i in range(nums_len):
                if i < nums_len - 1 and nums[i] == nums[i+1]: continue              
                if nums[i] != sys.maxsize:
                    temp = nums[i]
                    nums[i] = sys.maxsize
                    backtracking(ans, cur+[temp], cur_len+1, nums, nums_len)
                    nums[i] = temp
            
        
        ans = []
        nums.sort()
        backtracking(ans, [], 0, nums, len(nums))
        return ans