class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mark = [0 for i in xrange(len(nums))]
        ans = -1
        for num in nums:
            if mark[num] == 0:
                mark[num] = 1
                cnt = 1
                n = nums[num]
                while mark[n] == 0:
                    mark[n] = 1
                    n = nums[n]
                    cnt += 1
                if cnt > ans: ans = cnt
        return ans 