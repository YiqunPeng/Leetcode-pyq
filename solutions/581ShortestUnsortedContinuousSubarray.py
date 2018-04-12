class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ori = [item for item in nums]
        nums.sort()
        l, r = 0, 0
        for i in xrange(len(nums)):
            if nums[i] != ori[i]:
                l = i
                break
        for i in xrange(len(nums)-1, -1, -1):
            if nums[i] != ori[i]:
                r = i
                break
        return r - l + 1 if r != l else 0