class Solution:
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums_len = len(nums)
        ans = [-1] * nums_len
        if nums_len == 0: return []
        
        stack = [0]
        for i in range(1, nums_len):
            flag = 1
            while flag and stack:
                top = stack[-1]
                if nums[i] > nums[top]:
                    ans[top] = nums[i]
                    stack.pop(-1)
                else:
                    flag = 0
            stack.append(i)
        
        for i in stack:
            for j in range(0, i):
                if nums[j] > nums[i]:
                    ans[i] = nums[j]
                    break
        
        return ans