class Solution:
    def minTransfers(self, transactions):
        """
        :type transactions: List[List[int]]
        :rtype: int
        """
        def dfs(curr, debt):
            res = n = len(debt)
            
            while curr < n and debt[curr] == 0: curr += 1     
            if curr == n: return 0
            
            for i in range(curr + 1, n):
                if debt[i] * debt[curr] < 0:
                    debt[i] += debt[curr]
                    res = min(res, 1 + dfs(curr + 1, debt))
                    debt[i] -= debt[curr]
            
            return res
        
        
        ledge = collections.defaultdict(int)
        for t in transactions:
            ledge[t[0]] += t[2]
            ledge[t[1]] -= t[2]
            
        counter = collections.Counter(ledge.values())
        debt = []
        cnt = 0
        
        for k, v in counter.items():
            if not k: continue    
            if -k not in counter:
                for i in range(v):
                    debt.append(k)
            elif k in counter and v >= counter[-k]:
                cnt += counter[-k]
                for i in range(v - counter[-k]):
                    debt.append(k)
                counter[-k] = 0

        return dfs(0, debt) + cnt