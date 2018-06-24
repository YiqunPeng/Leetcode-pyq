class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        ans = sys.maxsize
        n = len(nums)
        if n == 0: return 0
        
        left, right = 0, 1
        sub_sum = nums[0]  
        while left <= right <= n:
            if sub_sum >= s:
                ans = min(ans, right - left)
                if ans == 1: return ans
                sub_sum -= nums[left]
                left += 1
            else:
                if right < n: sub_sum += nums[right]
                right += 1

        return ans if ans != sys.maxsize else 0
        