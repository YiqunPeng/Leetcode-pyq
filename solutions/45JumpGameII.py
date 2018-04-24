class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 1: return 0
        
        cur_max_pos = nums[0]
        next_max_pos = 0
        cur_pos = 0
        ans = 1
        
        while cur_max_pos < len(nums) - 1:
            for i in range(cur_pos, cur_max_pos + 1):
                next_max_pos = max(next_max_pos, nums[i] + i)
            cur_pos = cur_max_pos + 1
            cur_max_pos = next_max_pos
            ans += 1
                     
        return ans