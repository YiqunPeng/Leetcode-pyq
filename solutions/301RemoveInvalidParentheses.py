class Solution:
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def is_valid(s):
            cnt = 0
            for c in s:
                if c == '(':
                    cnt += 1
                elif c == ')':
                    if cnt > 0:
                        cnt -= 1
                    else:
                        return False
            return cnt == 0
            
        
        lvl = {s}
        while lvl:
            valid = []
            for s in lvl:
                if is_valid(s): valid.append(s)
            if valid: return valid
            lvl = {s[:i] + s[i+1:] for s in lvl for i in range(len(s))}
        
        return ['']  