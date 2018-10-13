class Solution:
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        row_used, col_used, diag_used, subdiag_used = set(), set(), set(), set()
        
        
        def can_place(r, c):
            return r not in row_used and c not in col_used and r + c not in subdiag_used and r - c not in diag_used
    
    
        def backtracking(row):
            if row == n: return 1
            
            res = 0
            for col in range(n):
                if can_place(row, col):
                    row_used.add(row)
                    col_used.add(col)
                    diag_used.add(row - col)
                    subdiag_used.add(row + col)
                    
                    res += backtracking(row + 1)
                    
                    subdiag_used.remove(row + col)
                    diag_used.remove(row - col)
                    col_used.remove(col)
                    row_used.remove(row)
            
            return res
            
            
        return backtracking(0)