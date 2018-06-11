class Solution:
    def shiftingLetters(self, S, shifts):
        """
        :type S: str
        :type shifts: List[int]
        :rtype: str
        """
        shift_len = len(shifts)
        shift_sum = [0] * shift_len
        shift_sum[-1] = shifts[-1]
        for i in range(shift_len-2, -1, -1):
            shift_sum[i] = shift_sum[i+1] + shifts[i]
        
        ans = ''
        for i in range(len(S)):
            c = chr((ord(S[i])-ord('a')+shift_sum[i])%26+ord('a'))
            ans = ans + c
            
        return ans