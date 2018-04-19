class Solution:
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        def swap(nums, i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            
        for i in range(len(nums)-1):
            if i % 2 == 0:
                if nums[i] > nums[i+1]:
                    swap(nums, i, i+1)
            else:
                if nums[i] < nums[i+1]:
                    swap(nums, i, i+1)
                