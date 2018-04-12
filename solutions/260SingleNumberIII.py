class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = 0
        x, y = 0, 0
        for num in nums:
            res ^= num
        p = 0
        while True:
            if res & (1 << p) != 0:
                break
            p += 1
        for num in nums:
            if num & (1 << p) != 0:
                x ^= num
            else:
                y ^= num
        return [x, y]