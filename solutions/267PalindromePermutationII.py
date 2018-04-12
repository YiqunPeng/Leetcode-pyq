class Solution:
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def backtracking(ans, cur, cur_len, half, half_len):
            if cur_len == half_len:
                ans.append(cur[:])
                return
            for i in range(half_len):
                if i > 0 and half[i] == half[i-1]: continue
                if half[i] != '':
                    temp = half[i]
                    half[i] = ''
                    backtracking(ans, cur+temp, cur_len+1, half, half_len)
                    half[i] = temp
                
        
        dic = {}

        for c in s:
            dic[c] = dic.get(c, 0) + 1
        odd = ''
        half = []
        for key in dic:
            if dic[key] % 2 == 1 and odd == '':
                odd = key
            elif dic[key] % 2 == 1 and odd != '':
                return []
            half = half + [key] * (dic[key] // 2)
        
        ans = []      
        backtracking(ans, '', 0, half, len(half))
        
        for i in range(len(ans)):
            ans[i] = ans[i] + odd + ans[i][::-1]
        
        return list(set(ans))
            
        
        
            