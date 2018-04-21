class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def is_palind(s, length):
            l, r = 0, length-1
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        
        def backtracking(ans, cur_list, cur_str, cur_len):
            if cur_len == 0:
                ans.append(cur_list)
                return
            if cur_len == 1:
                ans.append(cur_list + [cur_str])
                return 
            for i in range(1, cur_len+1):
                str = cur_str[0:i]
                if is_palind(str, i):
                    backtracking(ans, cur_list+[str], cur_str[i:], cur_len-i)
                    
 
        ans = []
        backtracking(ans, [], s, len(s))
        
        return ans
        