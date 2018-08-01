class Solution:
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def count_neighbors(x, y):
            neighbors = [(x-1,y-1), (x-1,y), (x-1,y+1), (x,y-1), (x,y+1), (x+1,y-1), (x+1,y), (x+1,y+1)]
            m, n = len(board), len(board[0])
            res = 0
            for i, j in neighbors:
                if not (0 <= i < m and 0 <= j < n):
                    continue
                if board[i][j] >= 1:
                    res += 1
            return res
            
        
        if not board or not board[0]: return
        m, n = len(board), len(board[0])
        
        for i in range(m):
            for j in range(n):
                cnt = count_neighbors(i, j)
                if board[i][j] == 1 and (cnt < 2 or cnt > 3):
                    board[i][j] = 2
                elif board[i][j] == 0 and cnt == 3:
                    board[i][j] = -1
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == -1:
                    board[i][j] = 1
                if board[i][j] == 2:
                    board[i][j] = 0
        