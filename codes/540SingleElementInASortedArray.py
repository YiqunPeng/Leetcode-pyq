class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def bin_search(nums, l, r):
            if l == r: return nums[l]
            mid = ((r-l)/2) + l
            if nums[mid] != nums[mid+1] and nums[mid] != nums[mid-1]: return nums[mid]
            if mid % 2 == 1:
                if nums[mid+1] == nums[mid]:
                    return bin_search(nums, l, mid-1)
                else:
                    return bin_search(nums, mid+1, r)
            else:
                if nums[mid+1] == nums[mid]:
                    return bin_search(nums, mid, r)
                else:
                    return bin_search(nums, l, mid)
                
        return bin_search(nums, 0, len(nums)-1)