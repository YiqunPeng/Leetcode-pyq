class Solution:
    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def dfs(nums): 
            if len(nums) == 1:
                if abs(nums[0] - 24) < 0.001:
                    return True
            
            for i in range(len(nums)):
                for j in range(i):
                    a, b = nums[i], nums[j]
                    
                    nums.pop(i)
                    nums.pop(j)
                    
                    nxt = [a+b, a-b, b-a, a*b]
                    if abs(a) > 0.001:
                        nxt.append(b / a)
                    if abs(b) > 0.001:
                        nxt.append(a / b)
                    
                    for n in nxt:
                        nums.append(n)
                        if dfs(nums):
                            return True
                        nums.pop()
                    
                    nums.insert(j, b)
                    nums.insert(i, a)
            
            return False

        return dfs(nums)