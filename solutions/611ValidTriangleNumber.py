from bisect import bisect_right

class Solution:
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        n = len(nums)
        nums.sort()
        
        for i in range(n):
            if nums[i] == 0: continue
            for j in range(i+1, n):
                val = nums[i] + nums[j] - 1
                pos = bisect_right(nums, val, j+1, n) - 1
                ans += pos - j
                
        return ans