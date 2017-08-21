class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        old_r = len(nums)
        old_c = len(nums[0])
        if old_r * old_c != r * c:
            return nums
        items = []
        res = []
        for o_r in range(old_r):
            for o_c in range(old_c):
                items.append(nums[o_r][o_c])
        pos = 0
        for n_r in range(r):
            temp = []
            for n_c in range(c):
                temp.append(items[pos])
                pos += 1
            res.append(temp)
        return res
