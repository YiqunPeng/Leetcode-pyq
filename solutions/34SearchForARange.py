class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """        
        def binary_search(nums, left, right, tar, ans):
            if left > right:
                return
            mid = (right - left) // 2 + left
            if nums[mid] == tar:
                if mid == 0 or nums[mid-1] != tar:
                    ans[0] = mid
                if mid == len(nums)-1 or nums[mid+1] != tar:
                    ans[1] = mid
                if (mid == 0 or nums[mid-1] != tar) and (mid == len(nums)-1 or nums[mid+1] != tar): 
                    ans[0] = mid
                    ans[1] = mid
                if ans[0] == -1 and mid > 0 and nums[mid-1] == tar:
                    binary_search(nums, left, mid-1, tar, ans)
                if ans[1] == -1 and mid < len(nums)-1 and nums[mid+1] == tar:
                    binary_search(nums, mid+1, right, tar, ans)
            elif nums[mid] < tar:
                binary_search(nums, mid+1, right, tar, ans)
            else:
                binary_search(nums, left, mid-1, tar, ans)
        
        ans = [-1, -1]
        binary_search(nums, 0, len(nums)-1, target, ans)
        return ans
            