class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums_len = len(nums)
        nums.sort()
        cl_sum = sys.maxsize
        ans = 0
        
        for i in range(nums_len):
            target = target - nums[i]
            left, right = 0, nums_len - 1
            while left < right:
                if left == i: 
                    left += 1
                    continue
                if right == i:
                    right -= 1
                    continue
                d = nums[left] + nums[right] - target
                if abs(d) < cl_sum:
                    cl_sum = abs(d)
                    ans = nums[left] + nums[right] + nums[i]
                if d < 0:
                    left += 1
                elif d > 0:
                    right -= 1
                else:
                    return ans
        
            target = target + nums[i]
        
        return ans
                
            
            
            