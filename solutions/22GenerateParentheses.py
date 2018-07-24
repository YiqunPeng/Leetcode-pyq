class Solution:
    # backtracking
    # time: O(2^n)
    # space: O(2^n)
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        
        def backtracking(l_n, r_n, s, stack):            
            if l_n == 0 and r_n == 0:
                ans.append(s)
            if l_n > 0:
                stack.append('(')
                backtracking(l_n-1, r_n, s+'(', stack)
                stack.pop(-1)
            if r_n > 0 and stack:
                stack.pop(-1)
                backtracking(l_n, r_n-1, s+')', stack)
                stack.append('(')       
        
        backtracking(n, n, '', [])
        return ans