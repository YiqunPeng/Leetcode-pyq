class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def binary_search(n, l, r, ans):
            if ans != -1 or l > r: return ans
            m = (l + r) // 2 
            if (m==0 or n[m]>n[m-1]) and (m==len(n)-1 or n[m]>n[m+1]):
                ans = m
            else:
                ans = binary_search(n, l, m-1, ans)
                ans = binary_search(n, m+1, r, ans)
            return ans
        
        if len(nums) == 1: return 0
                
        return binary_search(nums, 0, len(nums)-1, -1)
        
