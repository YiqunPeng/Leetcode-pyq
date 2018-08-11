class Solution:
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            
            if mid == len(nums)-1 or mid == 0 or (nums[mid-1] != nums[mid] != nums[mid+1]):
                return nums[mid]
            
            if mid % 2 == 0:
                if nums[mid] == nums[mid-1]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] == nums[mid+1]:
                    right = mid - 1
                else:
                    left = mid + 1
