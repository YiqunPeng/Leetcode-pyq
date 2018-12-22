class Solution:
    
    def __init__(self):
        self.memo = collections.defaultdict(list)
        self.ops = set(['+', '-', '*'])
        
    
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        if not input: return []
        res = []
        
        for idx, c in enumerate(input):
            if c in self.ops:
                if input[:idx] in self.memo:
                    l_res = self.memo[input[:idx]]
                else:
                    l_res = self.diffWaysToCompute(input[:idx])
                
                if input[idx+1:] in self.memo:
                    r_res = self.memo[input[idx+1:]]
                else:
                    r_res = self.diffWaysToCompute(input[idx+1:])
                
                for l in l_res:
                    for r in r_res:
                        if c == '-':
                            res.append(l - r)
                        elif c == '+':
                            res.append(l + r)
                        elif c == '*':
                            res.append(l * r)
                
        if not res:
            res.append(int(input))
        self.memo[input] = res
        return res