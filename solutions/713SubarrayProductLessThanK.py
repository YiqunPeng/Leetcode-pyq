class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans = 0
        
        p = 1
        left, right = 0, 0
        
        while right < len(nums):
            p *= nums[right]
            
            while left <= right and p >= k:
                p //= nums[left]
                left += 1
            
            ans += (right - left + 1)
            right += 1
        
        return ans