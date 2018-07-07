import queue

class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def bfs(x, y, o, border):
            m, n = len(board), len(board[0])
            if (x, y) in o: 
                o.remove((x, y))
            elif (x, y) in border:
                border.remove((x, y))
            q = queue.Queue()
            q.put((x, y))
            while not q.empty():
                x, y = q.get()
                for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                    if not (0 <= nx < m and 0 <= ny < n):
                        continue
                    if (nx, ny) in o:
                        o.remove((nx, ny))
                        q.put((nx, ny))
                    elif (nx, ny) in border:
                        border.remove((nx, ny))
                        q.put((nx, ny))
                    
        
        if not board or not board[0]: return
        
        border = set()
        o = set()
        
        m, n = len(board), len(board[0])
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                        border.add((i, j))
                    else:
                        o.add((i, j))
        
        while border:
            i, j = border.pop()
            bfs(i, j, o, border)
            
        for i, j in o:
            board[i][j] = 'X'
        