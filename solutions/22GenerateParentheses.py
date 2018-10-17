class Solution:
    # backtracking
    # time: O(2^n)
    # space: O(2^n)
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def backtracking(stack, curr, l, r):
            if l == r == 0: 
                ans.append(curr)
                return
            
            if stack and r > 0:
                stack.pop()
                backtracking(stack, curr + ')', l, r - 1)
                stack.append('(')

            if l > 0:
                stack.append('(')
                backtracking(stack, curr + '(', l - 1, r)
                stack.pop()              
            
               
        ans = []
        backtracking([], '', n, n)
        return ans