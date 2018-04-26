class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtracking(ans, cur, cur_len, nums, l):
            if cur_len == l:
                ans.append(cur)
                return
            
            for i in range(l):
                if nums[i] != sys.maxsize:
                    temp = nums[i]
                    nums[i] = sys.maxsize
                    backtracking(ans, cur+[temp], cur_len+1, nums, l)
                    nums[i] = temp
            
        ans = []
        backtracking(ans, [], 0, nums, len(nums))
        return ans