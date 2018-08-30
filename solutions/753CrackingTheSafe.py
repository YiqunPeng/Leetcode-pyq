class Solution:
    def crackSafe(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        def dfs(pwd, v, total):
            if len(v) == total:
                return True, pwd
            
            last = pwd[-n+1:] if -n + 1 != 0 else ''
            for i in range(k):
                nxt = last + str(i)
                if nxt not in v:
                    v.add(nxt)
                    
                    res, pwd = dfs(pwd+str(i), v, total)
                    if res: return True, pwd
                    
                    v.remove(nxt)
            
            return False, pwd[:-1]
        
        
        pwd = '0' * n
        visited = set([pwd])
        
        return dfs(pwd, visited, k ** n)[1]