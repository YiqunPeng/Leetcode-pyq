class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        cur_max = -sys.maxsize
        cur_cnt = 0
        for i in xrange(len(nums)):
            if nums[i] > cur_max:
                cur_max = nums[i]
                cur_cnt += 1
            else:
                if cur_cnt > ans:
                    ans = cur_cnt
                cur_cnt = 1
                cur_max = nums[i]
        return max(ans, cur_cnt)