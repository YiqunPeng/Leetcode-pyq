class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        left, right = 0, len(nums) - 1

        pos = 0
        while pos <= right:
            if nums[pos] == 0 and pos > left:
                nums[pos], nums[left] = nums[left], nums[pos]
                left += 1
            elif nums[pos] == 2:
                nums[pos], nums[right] = nums[right], nums[pos]
                right -= 1
            else:
                pos += 1
        