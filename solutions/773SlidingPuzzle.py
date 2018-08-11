class Solution:
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        def board_to_string(b):
            res = ''
            for i in range(2):
                for j in range(3):
                   res += str(b[i][j])
            return res
        
        def string_to_board(s):
            board = [['' for j in range(3)] for i in range(2)]
            for i in range(6):
                board[i//3][i%3] = s[i]
            return board

        x, y = -1, -1
        for i in range(2):
            for j in range(3):
                if board[i][j] == 0:
                    x, y = i, j
                    break
        
        visited = set()
        visited.add(board_to_string(board))
        
        queue = collections.deque()
        queue.append((board_to_string(board), x, y, 0))
        while queue:
            b, x, y, moves = queue.popleft()
            if b == '123450': return moves
            for nx, ny in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                if not (0 <= nx < 2 and 0 <= ny < 3): continue
                nboard = string_to_board(b)
                nboard[nx][ny], nboard[x][y] = nboard[x][y], nboard[nx][ny]
                nb = board_to_string(nboard)
                if nb not in visited:
                    queue.append((nb, nx, ny, moves+1))
                    visited.add(nb)
 
        return -1
            
