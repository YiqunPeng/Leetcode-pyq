class Solution:
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        n = len(board)
        mapping = {}
        k = 1
        i, j = n - 1, 0
        mode = 1
        while k <= n * n:
            mapping[k] = (i, j)
            k += 1
            if mode == 1:
                if j + 1 < n:
                    j += 1
                else:
                    i -= 1
                    j = n - 1
                    mode = 0
            else:
                if j - 1 >= 0:
                    j -= 1
                else:
                    i -= 1
                    j = 0
                    mode = 1

        q = collections.deque()
        q.append((1, 0))
        v = set()
        v.add(1)
        
        while q:
            idx, m = q.popleft()
            if idx == n * n:
                return m

            for i in range(1, 7):
                nxt = idx + i
                if nxt > n * n: break
                    
                ni, nj = mapping[nxt]
                if board[ni][nj] != -1:
                    nxt = board[ni][nj]

                if nxt not in v:
                    v.add(nxt)
                    q.append((nxt, m+1))
        
        return -1