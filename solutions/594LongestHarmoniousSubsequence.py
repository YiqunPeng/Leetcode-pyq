class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        
        dic = {}
        min_num, max_num = min(nums), max(nums)
        
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        
        har_sum = -1
        har_num = min_num
        
        for key in dic.keys():
            if not dic.has_key(key+1):
                continue
            else:
                temp_sum = dic[key] + dic[key+1]
                if temp_sum > har_sum:
                    har_sum = temp_sum
                    
        if har_sum != -1:
            return har_sum
        else:
            return 0