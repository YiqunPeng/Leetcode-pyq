class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        ops = set(['+', '-', '*', '/'])
        
        for t in tokens:
            if t not in ops:
                stack.append(int(t))
            else:
                b, a = stack.pop(), stack.pop()
                if t == '+':
                    stack.append(a + b)
                elif t == '-':
                    stack.append(a - b)
                elif t == '*':
                    stack.append(a * b)
                else:
                    sign = a // abs(a) * b // abs(b) if a * b != 0 else 0
                    stack.append(abs(a) // abs(b) * sign)
        
        return stack[0]