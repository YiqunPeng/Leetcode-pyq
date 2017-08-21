class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board
        if board[click[0]][click[1]] == 'E':
            cnt = self.count_mine(board, click)
            if cnt != 0:
                board[click[0]][click[1]] = str(cnt)
                return board
            else:
                board[click[0]][click[1]] = 'B'
                self.dfs(board, click)
                return board
    
    def dfs(self, board, pos):
        for i in xrange(-1, 2):
            for j in xrange(-1, 2):
                x = pos[0] + i
                y = pos[1] + j
                if i == 0 and j == 0: continue
                if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]): continue
                if board[x][y] == 'E':
                    cnt = self.count_mine(board, [x,y])
                    if cnt != 0:
                        board[x][y] = str(cnt)
                    else:
                        board[x][y] = 'B'
                        self.dfs(board, [x, y])    
        
    def count_mine(self, board, pos):
        cnt = 0
        for i in xrange(-1, 2):
            for j in xrange(-1, 2):
                x = pos[0] + i
                y = pos[1] + j
                if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]): continue
                if board[x][y] == 'M':
                    cnt += 1
        return cnt