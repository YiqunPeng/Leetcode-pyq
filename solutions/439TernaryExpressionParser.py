class Solution:
    def parseTernary(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        def dfs(exp):
            length = len(exp)
            if length == 1:
                return exp
            
            last_colon = -1
            stack = []
            for i in range(length-1, -1, -1):
                if exp[i] == ':':
                    stack.append(i)
                if exp[i] == '?':
                    last_colon = stack.pop(-1)
                    
            if exp[0] == 'T':
                return dfs(exp[2:last_colon])
            else:
                return dfs(exp[last_colon+1:])
            
        
        return dfs(expression)