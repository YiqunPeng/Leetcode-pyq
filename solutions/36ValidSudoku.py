class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        def valid_small(x, y):
            nums = [0] * 10
            for i in range(3):
                for j in range(3):
                    n_i, n_j = i+x, j+y
                    if board[n_i][n_j] == '.': continue
                    nums[int(board[n_i][n_j])] += 1
            for i in range(1, 10):
                if nums[i] > 1:
                    return False
            return True
            
        
        nums = [0] * 10
        for i in range(9):
            row = board[i]
            for c in row:
                if c == '.': continue
                nums[int(c)] += 1
            for j in range(1, 10):
                if nums[j] > 1:
                    return False
            nums = [0] * 10
        
        for j in range(9):
            for i in range(9):
                if board[i][j] == '.': continue
                nums[int(board[i][j])] += 1
            for k in range(1, 10):
                if nums[k] > 1:
                    return False
            nums = [0] * 10
        
        for i in range(3):
            for j in range(3):
                if not valid_small(i*3, j*3):
                    return False
        
        return True
        