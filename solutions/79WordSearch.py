class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def backtracking(b, w, x, y, l):
            if l == len(w):
                return True
            
            row, col = len(b), len(b[0])
            d = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            flag = False
            for i in d:
                n_x, n_y = x + i[0], y + i[1]
                if n_x >= 0 and n_x < row and n_y >= 0 and n_y < col and b[n_x][n_y] == w[l]:
                    temp = b[n_x][n_y]
                    b[n_x][n_y] = ''
                    flag = backtracking(b, w, n_x, n_y, l+1)
                    if flag:
                        return flag
                    b[n_x][n_y] = temp
            
            return False
                
                
        if not board or not word: return False
        
        flag = False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    board[i][j] = ''
                    flag = backtracking(board, word, i, j, 1)
                    board[i][j] = word[0]
                    if flag:
                        return flag
        
        return False