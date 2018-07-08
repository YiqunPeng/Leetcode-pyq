class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def union(n1, n2):
            f1, f2 = find(n1), find(n2)
            if f1 != f2:
                father[n1] = f2
        
        def find(n):
            if father[n] == n:
                return n
            father[n] = find(father[n])
            return father[n]    
        
        father = {}
        for num in nums:
            father[num] = num    
        nums_set = set(nums)
        
        for num in nums:
            if num - 1 in nums_set:
                union(num, num - 1)
        
        count = {}
        for num in father.keys():
            f = find(num)
            count[f] = count.get(f, 0) + 1     
        ans = 0
        for val in count.values():
            ans = max(ans, val)
        return ans
