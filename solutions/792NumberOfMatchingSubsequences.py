class Solution:
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        w_len = len(words)
        w_pos = [0] * w_len
                
        dic = {}
        for i in string.ascii_lowercase:
            dic[i] = []
            
        for i in range(w_len):
            dic[words[i][0]].append(i)
        
        for s in S:
            s_list = []   
            for i in range(len(dic[s])):
                w_i = dic[s][i]
                w_pos[w_i] += 1
                if w_pos[w_i] != len(words[w_i]):
                    if words[w_i][w_pos[w_i]] == s:
                        s_list.append(w_i)
                    else:
                        dic[words[w_i][w_pos[w_i]]].append(w_i)
            dic[s] = s_list
        
        ans = 0
        for key in dic:
            ans += len(dic[key])
        
        return w_len - ans
                    