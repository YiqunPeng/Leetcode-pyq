class Solution:
    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        def valid(pre_key, key, used):
            if not pre_key: return True
            px, py = (pre_key-1) // 3, (pre_key-1) % 3
            x, y = (key-1) // 3, (key-1) % 3
            if py == y and abs(px-x) == 2:
                return 4+y in used
            elif abs(py-y) == 2:
                if abs(px-x) == 2:
                    return 5 in used
                elif px == x:
                    return min(pre_key, key)+1 in used
            return True         
        
        def backtracking(res, used, length, used_set):
            if len(used) == length:
                res.append(used[:])
                return
            for i in range(1, 10):
                if i not in used_set and (not used or valid(used[-1], i, used)):
                    used_set.add(i)
                    backtracking(res, used+[i], length, used_set)
                    used_set.remove(i)     
            
        ans = 0      
    
        moves = []
        backtracking(moves, [], m, set())
        ans += len(moves)
        cnt = [0] * 10
        for move in moves:
            cnt[move[-1]] += 1
        print(cnt)
        
        for i in range(m+1, n+1):
            pre = []
            for move in moves:
                backtracking(pre, move, i, set(move))
            moves = pre
            ans += len(moves)
            cnt = [0] * 10
            for move in moves:
                cnt[move[-1]] += 1
            print(cnt)
        
        return ans

Solution().numberOfPatterns(1,3)