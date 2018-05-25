class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left, right = 1, 1
        num = len(nums)
        ans = [1 for i in range(num)]
        for i in range(num):
            ans[i] *= left;
            ans[num-1-i] *= right;
            left *= nums[i];
            right *= nums[num-1-i];
        return ans
