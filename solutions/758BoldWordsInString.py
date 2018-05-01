class Solution:
    def boldWords(self, words, S):
        """
        :type words: List[str]
        :type S: str
        :rtype: str
        """
        def mark_bold(mark, word, S):
            w_len = len(word)
            s_len = len(S)
            for i in range(s_len):
                if i + w_len <= s_len and S[i:i+w_len] == word:
                    for j in range(i, i+w_len):
                        mark[j] += 1
            
        
        s_len = len(S)
        mark = [0] * s_len
        
        for word in words:
            mark_bold(mark, word, S)

        ans = ''
        for i in range(s_len):
            if mark[i] >= 1 and (i == 0 or mark[i-1] == 0):
                ans = ans + '<b>'
            ans = ans + S[i]
            if mark[i] >= 1 and (i == s_len-1 or mark[i+1] == 0):
                ans = ans + '</b>'
        
        return ans
                