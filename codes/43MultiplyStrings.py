class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '0' or num2 == '0':
            return '0'
        
        l1, l2 = list(num1)[::-1], list(num2)[::-1]
        l1_len, l2_len = len(l1), len(l2)
        mul = [0] * (l1_len + l2_len + 1)
        
        for i in range(l1_len):
            pos = i
            for j in range(l2_len):
                mul[j + pos] += (int(l1[pos]) * int(l2[j]))
        
        for i in range(len(mul)-1):
            mul[i+1] += mul[i] // 10
            mul[i] = mul[i] % 10

        ans = ''
        leading_zero = True
        for i in range(len(mul)-1, -1, -1):
            if leading_zero and mul[i] == 0: 
                continue
            leading_zero = False
            ans = ans + str(mul[i])
        return ans