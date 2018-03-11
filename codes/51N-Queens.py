class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def add_to_ans(ans, b, N):
            n_b = []
            for i in range(N):
                temp = ''
                for j in range(N):
                    if b[i][j] == 0:
                        temp = temp + '.'
                    else:
                        temp = temp + 'Q'
                n_b.append(temp)
            ans.append(n_b)
            
        
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
            # print(ans)
            if n == N + 1:
                add_to_ans(ans, board, N)
                return 
            
            line = board[n-1]
            for i in range(N):
                if can_place(board, n-1, i, N):
                    line[i] = -1
                    backtracing(ans, board, n+1, N)
                    line[i] = 0

        
        ans = []
        board = [[0 for i in range(n)] for j in range(n)]
        backtracing(ans, board, 1, n)
        return ans