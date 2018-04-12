class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """      
        f_m, s_m, t_m = -sys.maxsize, -sys.maxsize, -sys.maxsize
        for num in nums:
            if num > f_m:
                t_m = s_m
                s_m = f_m
                f_m = num
            elif num < f_m and num > s_m:
                t_m = s_m
                s_m = num
            elif num < s_m and num > t_m:
                t_m = num
        
        return t_m if t_m != -sys.maxsize else max(nums)