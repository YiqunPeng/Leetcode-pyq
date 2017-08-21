class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        ans = 0
        row_len = len(board)
        col_len = len(board[0])
        
        for i in xrange(row_len):
            for j in xrange(col_len):
                if (board[i][j] == 'X') and (i == 0 or board[i-1][j] == '.') and (j == 0 or board[i][j-1] == '.'):
                    ans += 1
        
        return ans