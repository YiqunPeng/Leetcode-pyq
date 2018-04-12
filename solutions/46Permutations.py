class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtracing(ans, cur, nums, l):
            c = copy.deepcopy(cur)
            pos = len(c)
            if pos == l:
                ans.append(c)
                return
            
            for i in range(l):
                if nums[i] != sys.maxsize:
                    temp = nums[i]
                    c.append(temp)
                    nums[i] = sys.maxsize
                    backtracing(ans, c, nums, l)
                    nums[i] = temp
                    c.pop(-1)
            
        ans = []
        backtracing(ans, [], nums, len(nums))
        return anss