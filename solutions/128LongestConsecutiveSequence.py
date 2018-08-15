class Solution:
    # walk through
    # time: O(n)
    # space: O(n)
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        ans = 0
        
        for num in nums:
            if num + 1 not in nums:
                res = 1
                pre = num - 1
                while pre in nums:
                    pre -= 1
                    res += 1
                ans = max(ans, res)
        
        return ans
        
    # hash table
    # time: O(n)
    # space: O(n)
    # def longestConsecutive(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     nums = set(nums)
    #     dict = collections.defaultdict(int)

    #     ans = 0

    #     for num in nums:
    #         left, right = dict[num-1], dict[num+1]
    #         sum = left + right + 1

    #         ans = max(ans, sum)

    #         dict[num-left] = sum
    #         dict[num+right] = sum

    #     return ans
        
        
    # union find
    # time: O(n)
    # space: O(n)
    # def longestConsecutive(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     def union(n1, n2):
    #         f1, f2 = find(n1), find(n2)
    #         if f1 != f2: father[n1] = f2

    #     def find(n):
    #         if father[n] == n: return n
    #         father[n] = find(father[n])
    #         return father[n]    

    #     nums_set = set(nums)
    #     father = {}
    #     for num in nums_set:
    #         father[num] = num    

    #     for num in nums_set:
    #         if num - 1 in nums_set:
    #             union(num, num - 1)

    #     count = collections.defaultdict(int)
    #     for num in father.keys():
    #         count[find(num)] += 1    
    #     return max(count.values()) if count else 0
