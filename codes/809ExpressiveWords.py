class Solution:
    def expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        def compress(S):
            s_len = len(S)
            c_cnt = []
            if s_len > 0:
                s, c = '', S[0]
                cnt = 1
                for i in range(1, s_len):
                    if S[i] == c:
                        cnt += 1
                    else:
                        s = s + c
                        c_cnt.append(cnt)
                        cnt = 1
                        c = S[i]
                if cnt != 0:
                    s = s + c
                    c_cnt.append(cnt)
            return s, c_cnt
        
        [S, S_cnt] = compress(S)
        
        ans = 0
        for word in words:
            [word, w_cnt] = compress(word)
            flag = 1
            
            for i in range(len(word)):
                if len(word) != len(S):
                    flag = 0
                    break
                if word[i] != S[i]:
                    flag = 0
                    break
                if (S_cnt[i] < 3 and S_cnt[i] != w_cnt[i]) or (S_cnt[i] >= 3 and S_cnt[i] < w_cnt[i]):
                    flag = 0
                    break
            if flag:
                ans += 1
        
        return ans