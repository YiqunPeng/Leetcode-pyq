class Solution:
    def findMinMoves(self, machines):
        """
        :type machines: List[int]
        :rtype: int
        """
        d_sum = sum(machines)
        m_num = len(machines)
        
        if d_sum % m_num != 0: return -1
        
        avg = d_sum // m_num
        
        max_val = 0
        cnt = 0
        
        for m in machines:
            cnt += m - avg
            max_val = max([max_val, abs(cnt), m - avg])
            
        return max_val
            
        