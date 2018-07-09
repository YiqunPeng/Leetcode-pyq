class Solution:
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        def count_mines(x, y):
            m, n = len(board), len(board[0])
            adj = [(x-1,y-1), (x-1,y), (x-1,y+1), (x,y-1), (x,y+1), (x+1,y-1), (x+1,y), (x+1,y+1)]
            res = 0
            for nx, ny in adj:
                if not (0 <= nx < m and 0 <= ny < n): continue
                if board[nx][ny] == 'M':
                    res += 1
            return res
        
        def dfs(x, y):
            m, n = len(board), len(board[0])
            adj = [(x-1,y-1), (x-1,y), (x-1,y+1), (x,y-1), (x,y+1), (x+1,y-1), (x+1,y), (x+1,y+1)]
            for nx, ny in adj:
                if not (0 <= nx < m and 0 <= ny < n and board[nx][ny] == 'E'): continue
                cnt = count_mines(nx, ny)
                if cnt != 0:
                    board[nx][ny] = str(cnt)
                else:
                    board[nx][ny] = 'B'
                    dfs(nx, ny)
            
        
        cx, cy = click[0], click[1]
        if board[cx][cy] == 'M':
            board[cx][cy] = 'X'
        else:
            count = count_mines(cx, cy)
            if count != 0:
                board[cx][cy] = str(count)
            else:
                board[cx][cy] = 'B'
                dfs(cx, cy)
        return board
        