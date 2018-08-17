class Solution:
    # binary search
    # time: O(nlogn)
    # space: O(n)
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        
        n = len(nums)
        tail = [sys.maxsize] * n
        
        ans = 0
        for num in nums:
            l, r = 0, ans
            pos = -1
            while l <= r:
                m = l + (r - l) // 2
                if (m == 0 and num <= tail[m]) or (tail[m-1] < num <= tail[m]):
                    pos = m
                    break
                elif num > tail[m]:
                    l = m + 1
                else:
                    r = m - 1
            if pos == -1:
                ans += 1
                tail[ans] = num
            else:
                tail[pos] = num
        
        return ans + 1
        
    # dp
    # time: O(n^2)
    # space: O(n)
    # def lengthOfLIS(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     if not nums: return 0
    #     n = len(nums)

    #     dp = [1] * n

    #     for i in range(1, n):
    #         for j in range(0, i):
    #             if nums[i] > nums[j]:
    #                 dp[i] = max(dp[i], dp[j] + 1)

    #     return max(dp)