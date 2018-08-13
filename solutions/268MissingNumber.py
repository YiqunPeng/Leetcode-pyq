class Solution:
    # swap, two pass
    # time: O(n)
    # space: O(1)
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        for i in range(n):
            while nums[i] != n and nums[i] != i:
                a = nums[i]
                nums[i], nums[a] = nums[a], nums[i]
        
        for i in range(n):
            if nums[i] != i:
                return i
        return n

    # math
    # time: O(n)
    # space: O(1)
    # def missingNumber(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     n = len(nums)
    #     return n * (n + 1) // 2 - sum(nums)
