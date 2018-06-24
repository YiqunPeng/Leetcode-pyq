class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return True
            
            if nums[l] == nums[r]:
                l += 1
                continue

            if nums[l] <= nums[m]:
                if nums[m] > target and nums[l] <= target:
                    r = m - 1
                else:
                    l = m + 1
            elif nums[m] <= nums[r]:
                if nums[m] < target and nums[r] >= target:
                    l = m + 1
                else:
                    r = m - 1

        return False
                
        