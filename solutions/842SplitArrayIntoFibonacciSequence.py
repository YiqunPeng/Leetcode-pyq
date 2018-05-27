class Solution:
    def splitIntoFibonacci(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        s_len = len(S)
        
        for i in range(1, s_len-1):
            fi = S[0:i]
            if fi[0] == '0' and len(fi) != 1: break
            for j in range(i+1, s_len):
                se = S[i:j]
                if se[0] == '0' and len(se) != 1:
                    break
                temp = fi + se
                fi_v, se_v = int(fi), int(se)
                ans = [fi_v, se_v]
                while len(temp) < s_len:
                    s = fi_v + se_v
                    if s > 2 ** 31 - 1: break
                    temp = temp + str(s)
                    ans.append(s)
                    fi_v = se_v
                    se_v = s
                if temp == S:
                    return ans
        
        return []
                    
                
        