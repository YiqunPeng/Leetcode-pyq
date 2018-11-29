class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        
        while left <= right:
            if nums[left] <= nums[right]: return nums[left]
            
            mid = left + (right - left) // 2
            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid
                
        return nums[left]            