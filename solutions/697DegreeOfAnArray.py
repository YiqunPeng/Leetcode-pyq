class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        ans = sys.maxsize
        
        for i in range(0, len(nums)):
            if nums[i] not in dic.keys():
                dic[nums[i]] = [1, i, 1]
            else:
                dic[nums[i]][0] += 1
                dic[nums[i]][2] = i - dic[nums[i]][1] + 1
        
        values = [i[0] for i in dic.values()]
        degree = max(values)
        
        nums = []
        for key in dic.keys():
            if dic[key][0] == degree:
                nums.append(key)
        
        for num in nums:
            if dic[num][2] < ans:
                ans = dic[num][2]
        
        return ans