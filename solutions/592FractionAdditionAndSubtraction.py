class Solution(object):
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        def gcd(m, n):
            if n == 0: return m
            r = m % n
            while r != 0:
                m = n
                n = r
                r = m % n
            return n        
        
        num1, deno1 = 0, 1
        num2, deno2 = 0, 0
        sig, mark = 1, 0
        pos = 0
        while pos < len(expression):
            if expression[pos] == '+':
                sig = 1
                pos += 1
                continue
            if expression[pos] == '-':
                sig = -1
                pos += 1
                continue
            if expression[pos] == '/':
                mark = 1
                pos += 1
                continue
            if mark == 0:
                num2 = num2 * 10 + int(expression[pos])
            else:
                deno2 = deno2 * 10 + int(expression[pos])
            if (pos == len(expression)-1) or (expression[pos+1] in ['+', '-']):
                num1 = num1 * deno2 + sig * num2 * deno1
                deno1 = deno1 * deno2
                num2, deno2, mark = 0, 0, 0
            pos += 1
        div = gcd(abs(num1), abs(deno1))
        return str(num1/div) + '/' + str(deno1/div)