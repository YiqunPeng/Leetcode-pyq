class Solution:
    # xor
    # time: O(n)
    # space: O(1)
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        xor = 0
        for i in range(n + 1):
            xor ^= i

        for i in nums:
            xor ^= i

        return xor
    
    
    # sort 
    # time: O(nlogn)
    # space: O(1)
    # def missingNumber(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     nums.sort()
    #     i = 0 

    #     for num in nums:
    #         if num != i:
    #             return i
    #         i += 1

    #     return i
        
    
    # hashmap
    # time: O(n)
    # space: O(n)
    # def missingNumber(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """    
    #     n = len(nums)
    #     candid = set([i for i in range(n + 1)])

    #     for i in nums:
    #         candid.discard(i)

    #     return list(candid)[0]
    
    
    # math
    # time: O(n)
    # space: O(1)
    # def missingNumber(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     n = len(nums)
    #     return (1 + n) * n // 2 - sum(nums)        