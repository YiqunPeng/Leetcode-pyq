class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left, right = 1, 1
        ans = [1 for i in xrange(0, len(nums))]
        for i in xrange(1, len(nums)):
            left *= nums[i-1]
            ans[i] = left
        for i in xrange(len(nums)-2, -1, -1):
            right *= nums[i+1]
            ans[i] *= right
        return ans