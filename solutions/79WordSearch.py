class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board: return word == ''
        m, n = len(board), len(board[0])
        
        def dfs(i, j, word):
            if not word: return True
            
            res = False
            
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for d in directions:
                ni, nj = i + d[0], j + d[1]
                if 0 <= ni < m and 0 <= nj < n and board[ni][nj] == word[0] and (ni, nj) not in visited:
                    if len(word) == 1: return True
                    
                    visited.add((ni, nj))
                    res = res or dfs(ni, nj, word[1:])
                    visited.remove((ni, nj))
                    
                    if res: return True
            
            return res
            
        
        visited = set()
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    visited = set()
                    visited.add((i, j))
                    if dfs(i, j, word[1:]):
                        return True
                    
        return False