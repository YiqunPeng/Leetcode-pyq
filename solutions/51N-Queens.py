class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        col_used, row_used, diag_used, subdiag_used = set(), set(), set(), set()
        board = [['.'] * n for i in range(n)]
        
        ans = []        
        
        def can_place(x, y):
            return x not in row_used and y not in col_used and x + y not in subdiag_used and x - y not in diag_used
                   
        def backtracking(row):
            if row == n: 
                ans.append([''.join(board[i]) for i in range(n)])
                return
            for col in range(n):
                if can_place(row, col):
                    board[row][col] = 'Q'
                    col_used.add(col)
                    row_used.add(row)
                    subdiag_used.add(row + col)
                    diag_used.add(row - col)
                    
                    backtracking(row + 1)
                    
                    col_used.remove(col)
                    row_used.remove(row)
                    subdiag_used.remove(row + col)
                    diag_used.remove(row - col)
                    board[row][col] = '.'
                    

        backtracking(0)
        return ans