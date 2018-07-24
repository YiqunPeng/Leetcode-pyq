class Solution:
    # binary search, iterative
    # time: O(logn)
    # space: O(logn)
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """  
        ans = [-1, -1]
        
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right-left) // 2
            if nums[mid] == target:
                if mid == 0 or nums[mid-1] != target:
                    ans[0] = mid
                    break
                elif nums[mid-1] == target:
                    right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        if ans[0] == -1: return ans
        
        left, right = ans[0], len(nums)-1
        while left <= right:
            mid = left + (right-left) // 2
            if nums[mid] == target:
                if mid == len(nums)-1 or nums[mid+1] != target:
                    ans[1] = mid
                    break
                elif nums[mid+1] == target:
                    left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return ans
        

    # bianry search, recursive
    # time: O(logn)
    # space: O(logn)
    # def searchRange(self, nums, target):
    #     """
    #     :type nums: List[int]
    #     :type target: int
    #     :rtype: List[int]
    #     """
    #     ans = [-1, -1]

    #     def binary_search(nums, left, right):
    #         if left > right:
    #             return    
    #         mid = (right - left) // 2 + left
    #         if nums[mid] == target:
    #             if mid == 0 or nums[mid-1] != target:
    #                 ans[0] = mid
    #             if mid == len(nums)-1 or nums[mid+1] != target:
    #                 ans[1] = mid
    #             if ans[0] == -1 and mid > 0 and nums[mid-1] == target:
    #                 binary_search(nums, left, mid-1)
    #             if ans[1] == -1 and mid < len(nums)-1 and nums[mid+1] == target:
    #                 binary_search(nums, mid+1, right)
    #         elif nums[mid] < target:
    #             binary_search(nums, mid+1, right)
    #         else:
    #             binary_search(nums, left, mid-1)

    #     binary_search(nums, 0, len(nums)-1)
    #     return ans
            