class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def binary_search(nums, t, left, right):
            if left > right:
                return -1
            mid = left + (right - left) // 2
            if nums[mid] == t:
                return mid
            elif nums[mid] < t:
                if nums[mid] > nums[right]:
                    return binary_search(nums, t, mid+1, right)
                else:
                    if nums[right] >= t:
                        return binary_search(nums, t, mid+1, right)
                    else:
                        return binary_search(nums, t, left, mid-1)
            else:
                if nums[mid] < nums[left]:
                    return binary_search(nums, t, left, mid-1)
                else:
                    if nums[left] <= t:
                        return binary_search(nums, t, left, mid-1)
                    else:
                        return binary_search(nums, t, mid+1, right)
                  
        return binary_search(nums, target, 0, len(nums)-1)
        
        