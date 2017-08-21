class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        
        ans = 0
        dig = int(math.log(max(nums), 2)) + 1
        num = len(nums)
        for i in xrange(dig):
            cnt = 0
            for j in xrange(num):
                if nums[j] % 2 == 1:
                    cnt += 1
                nums[j] /= 2
            ans += (num-cnt) * cnt
        return ans