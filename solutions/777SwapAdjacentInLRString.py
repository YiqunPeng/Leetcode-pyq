class Solution:
    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        if len(start) != len(end): return False
        
        start_r = start.replace('X', '')
        end_r = end.replace('X', '')
        if start_r != end_r: return False
        
        s_r, s_l = [], []
        e_r, e_l = [], []
        for i in range(len(start)):
            if start[i] == 'R':
                s_r.append(i)
            elif start[i] == 'L':
                s_l.append(i)
        for i in range(len(end)):
            if end[i] == 'R':
                e_r.append(i)
            elif end[i] == 'L':
                e_l.append(i)

        if len(s_r) != len(e_r): return False
        if len(s_l) != len(e_l): return False
        
        for i in range(len(s_r)):
            if s_r[i] > e_r[i]: return False
        for i in range(len(s_l)):
            if s_l[i] < e_l[i]: return False
            
        return True
        
        
        