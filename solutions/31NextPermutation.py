class Solution:
    # math, reverse sort
    # time: O(n)
    # space: O(1)
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        pos = 0
        
        for i in range(n - 1, 0, -1):
            if nums[i] > nums[i-1]:
                pos = i
                break
                
        if pos > 0:
            for i in range(n - 1, pos - 1, -1):
                if nums[i] > nums[pos-1]: 
                    nums[pos-1], nums[i] = nums[i], nums[pos-1]  
                    break
                
        left, right = pos, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left, right = left + 1, right - 1

    # previous permutation
    # reverse sort
    # time: O(n)
    # space: O(1)
    # def previousPermutation(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: void Do not return anything, modify nums in-place instead.
    #     """
    #     n = len(nums)
    #     pos = 0

    #     for i in range(n - 1, 0, -1):
    #         if nums[i] < nums[i-1]:
    #             pos = i
    #             break

    #     if pos > 0:
    #         max_pos = 0
    #         for i in range(n - 1, pos - 1, -1):
    #             if nums[i] < nums[pos-1]:
    #                 max_pos = i
    #                 break
    #         nums[pos-1], nums[max_pos] = nums[max_pos], nums[pos-1]

    #     left, right = pos, n - 1
    #     while left < right:
    #         nums[left], nums[right] = nums[right], nums[left]
    #         left, right = left + 1, right - 1
