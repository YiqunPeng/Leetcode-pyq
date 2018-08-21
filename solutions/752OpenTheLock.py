class Solution(object):
    # bfs
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        deadends = set(deadends)
        if '0000' in deadends: return -1
        
        queue = collections.deque([('0000', 0)])
        while queue:
            lock, moves = queue.popleft()
            if lock == target:
                return moves
            
            for i in range(4):
                n_lock = lock[0:i] + str((int(lock[i]) + 1) % 10) + lock[i+1:]
                p_lock = lock[0:i] + str((int(lock[i]) - 1) % 10) + lock[i+1:]
                
                if n_lock not in deadends: 
                    queue.append((n_lock, moves + 1))
                    deadends.add(n_lock)
                if p_lock not in deadends: 
                    queue.append((p_lock, moves + 1))
                    deadends.add(p_lock)
        
        return -1         
