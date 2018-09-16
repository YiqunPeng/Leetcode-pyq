class Solution:
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        def win(board, pawn):
            c, r = [0] * 3, [0] * 3
            d = [0] * 2
            
            for i in range(3):
                for j in range(3):
                    if board[i][j] == pawn:
                        c[j] += 1
                        r[i] += 1
                        if i == j: d[0] += 1
                        if i + j == 2: d[1] += 1
                            
            return True if any(i == 3 for i in (c + r + d)) else False

        
        x, o, e = 0, 0, 0
        for i in range(3):
            for j in range(3):
                if board[i][j] == 'X':
                    x += 1
                elif board[i][j] == 'O':
                    o += 1
                else:
                    e += 1

        if x - o < 0 or x - o > 1: return False
        
        x_w = win(board, 'X')
        o_w = win(board, 'O')
        
        if x == o and x_w: return False
        if x == o + 1 and o_w: return False
        
        return True