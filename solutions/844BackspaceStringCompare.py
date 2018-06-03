class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        s_s, t_s = [], []
        
        for s in S:
            if s == '#':
                if s_s: s_s.pop()
            else:
                s_s.append(s)
        for t in T:
            if t == '#':
                if t_s: t_s.pop()
            else:
                t_s.append(t)
        
        return s_s == t_s