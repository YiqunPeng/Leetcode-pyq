class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        
        digits = set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
        
        sign = 1
        val = 0
        curr = 0
        stack = []
        
        for c in s:
            if c in digits:
                curr = curr * 10 + int(c)
            elif c == '+':
                val = val + sign * curr
                curr = 0
                sign = 1
            elif c == '-':
                val = val + sign * curr
                curr = 0
                sign = -1
            elif c == '(':
                stack.append(val)
                stack.append(sign)
                sign = 1
                val = 0
            elif c == ')':
                val = val + sign * curr
                curr = 0
                val = val * stack.pop()
                val = val + stack.pop()
        
        if curr != 0: 
            val += curr * sign
        return val               