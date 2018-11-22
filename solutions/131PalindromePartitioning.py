class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """ 
        def backtracking(ans, curr_part, re_str):
            re_len = len(re_str)
            if re_len == 0:
                ans.append(curr_part)
                return
            for i in range(1, re_len + 1):
                part = re_str[:i]
                if part == part[::-1]:
                    backtracking(ans, curr_part + [part], re_str[i:])
                    
 
        ans = []
        backtracking(ans, [], s)
        
        return ans  