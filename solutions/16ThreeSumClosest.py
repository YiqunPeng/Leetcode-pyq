class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        diff, ans = None, None   
        nums.sort()
        
        for i, num in enumerate(nums):
            left, right = i + 1, len(nums) - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                
                if not diff or abs(s - target) < diff:
                    diff = abs(s - target)
                    ans = s
                
                if s == target: 
                    return ans
                elif s > target:
                    right -= 1
                else:
                    left += 1
        
        return ans