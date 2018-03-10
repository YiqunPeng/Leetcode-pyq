class Solution:
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        def can_place(board, row, col, N):
            for i in range(N):
                if i == col: continue
                if board[row][i] == -1:
                    return False
                              
            for i in range(N):
                if i == row: continue
                if board[i][col] == -1:
                    return False
                if col-row+i < N and col-row+i >= 0 and board[i][col-row+i] == -1:
                    return False
                if col+row-i < N and col+row-i >= 0 and board[i][col+row-i] == -1:
                    return False 
                
            return True
                           
        
        def backtracing(ans, board, n, N):
            if n == N + 1:
                return ans + 1
            
            line = board[n-1]
            for i in range(N):
                if can_place(board, n-1, i, N):
                    line[i] = -1
                    ans = backtracing(ans, board, n+1, N)
                    line[i] = 0
            
            return ans
        
        board = [[0 for i in range(n)] for j in range(n)]
        return backtracing(0, board, 1, n)