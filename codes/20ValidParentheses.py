class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        p_stack = []
        for c in s:
            if c in ['(', '[', '{']:
                p_stack.append(c)
            else:
                if len(p_stack) == 0:
                    return False
                temp = p_stack.pop(-1)
                if (c == ')' and temp != '(') or (c == ']' and temp != '[') or (c == '}' and temp != '{'):
                    return False
        if len(p_stack) != 0:
            return False
        
        return True