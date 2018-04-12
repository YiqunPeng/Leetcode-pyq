class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        def less_than_k(l, i, k):
            for item in l:
                if abs(item-i) <= k:
                    return True
            return False
        
        
        nums_len = len(nums)
        dic = {}
        for i in range(nums_len):
            if nums[i] in dic:
                if less_than_k(dic[nums[i]], i, k):
                    return True
                dic[nums[i]].append(i)
            else:
                dic[nums[i]] = [i]
        
        return False