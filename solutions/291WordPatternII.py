class Solution:
    def __init__(self):
        self.ans = False
    
    def wordPatternMatch(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        p2w, w2p = {}, {}
        
        def backtracking(pat, str):
            if self.ans: 
                return
            if not pat and not str:
                self.ans = True
                return 
            if (not pat and str) or (pat and not str):
                return
            
            p = pat[0]
            if p in p2w:
                if str[:len(p2w[p])] != p2w[p]:
                    return
                else:
                    backtracking(pat[1:], str[len(p2w[p]):])
            else:
                for i in range(1, len(str)+1):
                    t_str = str[0:i]
                    if t_str in w2p: continue
                    p2w[p] = t_str
                    w2p[t_str] = p
                    backtracking(pat[1:], str[i:])
                    if self.ans: break
                    del p2w[p]
                    del w2p[t_str]
                    
   
        backtracking(pattern, str)
        return self.ans
