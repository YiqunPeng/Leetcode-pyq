class Solution:
    def minIncrementForUnique(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        ans = 0
        A.sort()
        max_v = -1
        
        for num in A:
            if num > max_v:
                max_v = num
            else:
                ans = ans + (max_v + 1 - num)
                max_v = max_v + 1
        
        return ans