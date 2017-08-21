class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        pos = 0
        for i in xrange(len(nums)):
            if nums[i] == 0:
                continue
            else:
                nums[pos] = nums[i]
                if pos != i:
                    nums[i] = 0
                pos += 1