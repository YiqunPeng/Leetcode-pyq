class Solution:
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        nums = []
        ans, flag, cnt = 0, int(s[0]), 1
        
        for i in s[1:]:
            if int(i) == flag:
                cnt += 1
            else:
                nums.append(cnt)
                flag = 1 - flag
                cnt = 1
        nums.append(cnt)
        
        for i in range(0, len(nums)-1):
            ans += (min(nums[i], nums[i+1]))
            
        return ans