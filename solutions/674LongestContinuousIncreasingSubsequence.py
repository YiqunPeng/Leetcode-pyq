class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        ans = 1
        n = len(nums)
        
        pre = 0
        cnt = 1
        for i in range(1, n):
            if nums[i] > nums[pre]:
                cnt += 1
            else:
                ans = max(cnt, ans)
                cnt = 1
            pre = i
        
        return max(ans, cnt)
        