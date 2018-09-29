class Solution:
    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
        triples = [[set() for j in range(7)] for i in range(7)]
        for a in allowed:
            f, s, t = ord(a[0]) - ord('A'), ord(a[1]) - ord('A'), a[2]
            triples[f][s].add(t)
            
        v = set()
            
        def dfs(string):
            if len(string) == 1:
                return True
            
            v.add(string)
            f, s = ord(string[0]) - ord('A'), ord(string[1]) - ord('A')
            nxt_string = [i for i in triples[f][s]]
            for i in range(1, len(string) - 1):
                nxt = []
                f, s = ord(string[i]) - ord('A'), ord(string[i+1]) - ord('A')
                for t in triples[f][s]:
                    for n in nxt_string:
                        nxt.append(n + t)
                nxt_string = nxt

            for n in nxt_string:
                if n not in v:
                    v.add(n)
                    if dfs(n):
                        return True           
            return False
            
        return dfs(bottom)