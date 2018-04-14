class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        def reverse(nums, s, e):
            l, r = s, e
            while l < r:
                temp = nums[l]
                nums[l] = nums[r]
                nums[r] = temp
                l += 1
                r -= 1
        
        k = k % len(nums)
        reverse(nums, 0, len(nums)-1)
        reverse(nums, 0, k-1)
        reverse(nums, k, len(nums)-1)
        
        
        
        
            
            