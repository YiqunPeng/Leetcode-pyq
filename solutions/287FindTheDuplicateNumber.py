class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) - 1
        
        left, right = 1, n
        
        while left <= right:
            if left == right:
                return left
            if right - left == 1:
                r_cnt, l_cnt = 0, 0
                for num in nums:
                    if num == left: l_cnt += 1
                    if num == right: r_cnt += 1
                return left if l_cnt > 1 else right 
            mid = left + (right - left) // 2
            cnt = 0
            for num in nums:
                if num <= mid:
                    cnt += 1
            if cnt <= mid:
                left = mid
            else:
                right = mid
        
        