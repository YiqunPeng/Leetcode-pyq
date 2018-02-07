class Solution:
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        ans = []
        
        s_hash = {}
        s_len = len(S)
        for i in range(s_len):
            s_hash[S[i]] = i
        
        start, end, cur = 0, 0, 0
        while cur < s_len:
            c = S[cur]
            end = max(end, s_hash[c])
            if end == cur and s_hash[c] == end:
                ans.append(end - start + 1)
                start = end + 1
                cur += 1
                continue
            cur += 1
        
        if end - start + 1 != 0:
            ans.append(end - start + 1)
        
        return ans
                
                
            
            
            