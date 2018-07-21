class Solution():
    # stack
    # time: O(n)
    # space: O(n)
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic = {'(': 1, '[': 2, '{': 3, ')': -1, ']': -2, '}': -3}
        
        stack = []
        for c in s:
            if dic[c] > 0:
                stack.append(dic[c])
            else:
                if not stack: return False
                if stack[-1] + dic[c] != 0: 
                    return False
                else:
                    stack.pop()
        
        return stack == []