class TicTacToe:

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.rows = [[0, 0] for i in range(n)]
        self.cols = [[0, 0] for i in range(n)]
        self.diags = [[0, 0], [0, 0]]
        self.n = n
        

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        pos = player - 1
        self.rows[row][pos] += 1
        self.cols[col][pos] += 1
        if row == col:
            self.diags[0][pos] += 1
        if row + col == self.n - 1:
            self.diags[1][pos] += 1
        
        if self.rows[row][pos] == self.n or self.cols[col][pos] == self.n:
            return player
        if self.diags[0][pos] == self.n or self.diags[1][pos] == self.n:
            return player
        return 0
            
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)