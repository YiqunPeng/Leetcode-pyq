class Solution:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        if nums[0] != 0:
            res = {nums[0]: 1, -nums[0]: 1}
        else:
            res = {nums[0]: 2}
          
        for i in range(1, len(nums)):
            new_res = {}
            for key in res:
                if nums[i] != 0:
                    new_res[key+nums[i]] = new_res.get(key+nums[i], 0) + res[key]
                    new_res[key-nums[i]] = new_res.get(key-nums[i], 0) + res[key]
                else:
                    new_res[key] = new_res.get(key, 0) + res[key] * 2
            res = new_res
            
        return res[S] if S in res else 0