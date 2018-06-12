class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        s_ptr, t_ptr = len(S) - 1, len(T) - 1
        s_bs, t_bs = 0, 0
        
        while s_ptr >= 0 or t_ptr >= 0:
            while s_ptr >= 0 and (S[s_ptr] == '#' or s_bs > 0):
                if S[s_ptr] == '#':
                    s_bs += 1
                elif S[s_ptr] != '#' and s_bs > 0:
                    s_bs -= 1
                s_ptr -= 1
            while t_ptr >= 0 and (T[t_ptr] == '#' or t_bs > 0):
                if T[t_ptr] == '#':
                    t_bs += 1
                elif T[t_ptr] != '#' and t_bs > 0:
                    t_bs -= 1
                t_ptr -= 1

            if t_ptr == -1 and s_ptr == -1:
                return True
            if t_ptr == -1 or s_ptr == -1:
                return False

            if S[s_ptr] == T[t_ptr]:
                s_ptr -= 1
                t_ptr -= 1
            else:
                return False

        return True if s_ptr == t_ptr else False
        