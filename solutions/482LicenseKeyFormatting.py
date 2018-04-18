class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        ans = ''
        cnt = K
        s_len = len(S)
        
        ord_0, ord_9 = ord('0'), ord('9')
        ord_a, ord_z = ord('a'), ord('z')
        ord_A, ord_Z = ord('A'), ord('Z')
        
        for i in range(s_len-1, -1, -1):
            if S[i] == '-': continue
            
            ord_i = ord(S[i])
            if (ord_i >= ord_0 and ord_i <= ord_9) or (ord_i >= ord_A and ord_i <= ord_Z):
                if cnt == 0:
                    ans = ans + '-'
                    cnt = K
                ans = ans + S[i]
                cnt -= 1
            elif ord_i >= ord_a and ord_i <= ord_z:
                if cnt == 0:
                    ans = ans + '-'
                    cnt = K
                ans = ans + chr(ord_A + ord_i - ord_a)
                cnt -= 1
        
        return ans[::-1]

        
        