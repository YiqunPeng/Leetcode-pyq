class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def backtracking(ans, l_n, r_n, s, stack):            
            if l_n == 0 and r_n == 0:
                ans.append(s)
            if l_n > 0:
                stack.append('(')
                backtracking(ans, l_n-1, r_n, s+'(', stack)
                stack.pop(-1)
            if r_n > 0 and stack:
                stack.pop(-1)
                backtracking(ans, l_n, r_n-1, s+')', stack)
                stack.append('(')       
        
        ans = []
        backtracking(ans, n, n, '', [])
        return ans