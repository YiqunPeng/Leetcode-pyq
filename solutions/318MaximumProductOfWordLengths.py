class Solution:
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        ans = 0
        words_len = len(words)
        words_dic = [{} for i in range(words_len)]
        
        for i in range(words_len):
            for j in words[i]:
                if j in words_dic[i]:
                    continue
                words_dic[i][j] = 1
                
        for i in range(words_len):
            for j in range(i+1, words_len):
                flag = 0
                for c in words_dic[j]:
                    if c in words_dic[i]:
                        flag = 1
                        break
                if flag == 0:
                    ans = max(ans, len(words[i] * len(words[j])))
        
        return ans