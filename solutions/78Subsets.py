class Solution:
    # backtracking/recursion
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtracking(ans, s_set, r_nums, s_len, t_len):
            if s_len == t_len:
                ans.append(s_set)
                return
            for i in range(len(r_nums)):
                backtracking(ans, s_set+[r_nums[i]], r_nums[i+1:], s_len+1, t_len)
            
        
        ans = [[]]
        
        for i in range(1, len(nums)+1):
            backtracking(ans, [], nums, 0, i)
            
        return ans
    
    # bit manipulation
    # def subsets(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: List[List[int]]
    #     """
    #     n = len(nums)
    #     bits = [bin(i)[2:] for i in range(2**n)]
        
    #     ans = []
    #     for bit in bits:
    #         sub = []
    #         for i in range(1, len(bit)+1):
    #             if bit[-i] == '1':
    #                 sub.append(nums[-i])
    #         ans.append(sub)
        
    #     return ans