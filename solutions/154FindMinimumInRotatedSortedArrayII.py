class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)        
        left, right = 0, n - 1
        
        while left < right:
            if nums[left] == nums[right]:
                left += 1
                continue
            if nums[left] < nums[right]:
                return nums[left]
            
            mid = left + (right - left) // 2
            if nums[left] <= nums[mid]:
                left = mid + 1
            else:
                right = mid
            
        return nums[left]   