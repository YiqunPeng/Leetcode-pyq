class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        paths = path.split('/')
        
        stack = []
        for path in paths:
            if path == '' or path == '.' or (path == '..' and len(stack) == 0): 
                continue
            elif path == '..' and len(stack) > 0:
                stack.pop(-1)
            else:
                stack.append(path)
        
        ans = '/'
        for i in stack:
            if ans[-1] != '/':
                ans += '/'
            ans += i
        
        return ans