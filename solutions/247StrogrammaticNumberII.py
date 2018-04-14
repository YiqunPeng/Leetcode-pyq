class Solution:
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def rotated_string(s):
            dic = {'0': '0', '1': '1', '6' : '9', '8': '8', '9': '6'}
            res = ''
            for i in range(len(s)-1, -1, -1):
                res = res + dic[s[i]]
            return res
                
        
        def backtracking(ans, cur, cur_len, half_len, stro_nums):
            if cur_len == half_len:
                ans.append(cur)
                return
            for i in range(len(stro_nums)):
                if cur_len == 0 and stro_nums[i] == '0': continue
                backtracking(ans, cur+stro_nums[i], cur_len+1, half_len, stro_nums)
         
        if n == 0: return []
            
        stro_nums = ['0', '1', '6', '8', '9']
        single_stro_nums = ['0', '1', '8']
        
        ans = []
        backtracking(ans, '', 0, n//2, stro_nums)
        
        temp = []
        if n % 2 == 0:
            for a in ans:
                temp.append(a + rotated_string(a))
        else:
            for a in ans:
                for num in single_stro_nums:
                    temp.append(a + num + rotated_string(a))
        
        return temp