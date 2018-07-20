class Solution:
    # Hash + without sorting
    # TLE 311/313 cases passed
    # time: O(n^2) 
    # space: O(n)
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        
        dic = {}
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        
        nums_set = set(nums)
        pair = set()
        n = len(nums)
        for i in range(n-2):
            dic[nums[i]] -= 1
            if dic[nums[i]] == 0: del dic[nums[i]]
            if nums[i] not in nums_set: continue
            nums_set.remove(nums[i])
            for j in range(i+1, n-1):
                if (nums[i], nums[j]) in pair or (nums[j], nums[i]) in pair: continue
                dic[nums[j]] -= 1
                if -nums[i]-nums[j] in dic and dic[-nums[i]-nums[j]] > 0:
                    ans.append([nums[i], nums[j], -nums[i]-nums[j]])
                    pair.add((nums[i], nums[j]))
                    pair.add((nums[j], -nums[i]-nums[j]))
                    pair.add((nums[i], -nums[i]-nums[j]))
                dic[nums[j]] += 1
        
        return ans
        

    # sort + two pointer
    # time: O(n^2)
    # space: O(1)
    # def threeSum(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: List[List[int]]
    #     """
    #     ans = []

    #     nums.sort()
    #     nums_len = len(nums)

    #     for i in range(nums_len - 2):
    #         if i > 0 and nums[i] == nums[i-1]: continue
    #         l, r = i + 1, nums_len - 1
    #         while l < r:
    #             s = nums[l] + nums[r] + nums[i]
    #             if s == 0:
    #                 ans.append([nums[l], nums[r], nums[i]])
    #                 l += 1
    #                 r -= 1
    #                 while nums[l] == nums[l-1] and l < nums_len - 1: l += 1
    #                 while nums[r] == nums[r+1] and r > i: r -= 1
    #             elif s > 0:
    #                 r -= 1
    #             else:
    #                 l += 1

    #     return ans
                                
        
        
        