class Solution:
    # iterative
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = [[]]
        
        for num in nums:
            nxt = []
            for a in ans:
                for i in range(len(a) + 1):
                    nxt.append(a[:i] + [num] + a[i:])
            ans = nxt
            
        return ans
        
    
    
    # backtracking (recursion)
    # def permute(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: List[List[int]]
    #     """
    #     def backtracking(ans, curr, remain):
    #         if not remain:
    #             ans.append(curr)        
    #         for i in range(len(remain)):
    #             backtracking(ans, curr + [remain[i]], remain[:i] + remain[i+1:])


    #     ans = []
    #     backtracking(ans, [], nums)
    #     return ans