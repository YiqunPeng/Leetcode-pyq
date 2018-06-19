class Solution:
    def candyCrush(self, board):
        """
        :type board: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(board), len(board[0])
        
        done = False
        while not done:
            done = True
            blocks = set()
            for i in range(m-1, -1, -1):
                for j in range(n):
                    if board[i][j] == 0: continue
                    if j + 2 < n:
                        if board[i][j] == board[i][j+1] and board[i][j] == board[i][j+2]:
                            done = False
                            blocks.add((i, j+1))
                            blocks.add((i, j+2))
                            blocks.add((i, j))
                            pos = j + 3
                            while pos < n:
                                if board[i][j] == board[i][pos]:
                                    blocks.add((i, pos))
                                    pos += 1
                                else:
                                    break
                    if i - 2 >= 0:
                        if board[i][j] == board[i-1][j] and board[i][j] == board[i-2][j]:
                            done = False
                            blocks.add((i-1, j))
                            blocks.add((i-2, j))
                            blocks.add((i, j))
                            pos = i - 3
                            while pos >= 0:
                                if board[pos][j] == board[i][j]:
                                    blocks.add((pos, j))
                                    pos -= 1
                                else:
                                    break
            for b in blocks:
                board[b[0]][b[1]] = 0

            for j in range(n):
                pos = m - 1
                for i in range(m-1, -1, -1):
                    if board[i][j] != 0:
                        if pos != i:
                            board[pos][j] = board[i][j]
                            board[i][j] = 0
                        pos -= 1

        return board