class Solution:
    # Hash 
    # time: O(n^2)
    # space: O(n^2)
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        cols = [set() for j in range(9)]
        rows = [set() for i in range(9)]
        blocks = [[set() for j in range(3)] for i in range(3)]
        
        for i in range(9):
            for j in range(9):
                char = board[i][j]
                if char != '.':
                    if char in cols[j] or char in rows[i] or char in blocks[i//3][j//3]:
                        return False
                    cols[j].add(char)
                    rows[i].add(char)
                    blocks[i//3][j//3].add(char)
        
        return True
