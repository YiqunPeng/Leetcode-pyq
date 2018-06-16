class Trie:
    def __init__(self, node):
        self.root = node
    
    def add(self, word):
        node = self.root
        for i in range(len(word)):
            if word[i] in node.children:
                node = node.children[word[i]]
            else:
                n_node = TrieNode(word[i])
                node.children[word[i]] = n_node
                node = n_node
            if i == len(word) - 1:
                node.is_word = True
            

class TrieNode:
    def __init__(self, v):
        self.v = v
        self.children = {}
        self.is_word = False


class Solution:
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        ans = []
        visited = [[False for j in range(len(board[0]))] for i in range(len(board))]
        
        def backtracking(x, y, node, word, m, n):
            if node.is_word:
                ans.append(word)
                node.is_word = False
                        
            for n_x, n_y in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                if not (0 <= n_x < m and 0 <= n_y < n): continue
                if visited[n_x][n_y]: continue
                if board[n_x][n_y] not in node.children: continue
                visited[n_x][n_y] = True
                c = board[n_x][n_y]
                backtracking(n_x, n_y, node.children[c], word+c, m, n)
                visited[n_x][n_y] = False
      
    
        if not board or not words: return []
        
        root = TrieNode('')
        trie = Trie(root)
        for word in words:
            trie.add(word)

        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] in root.children:
                    visited[i][j] = True
                    backtracking(i, j, root.children[board[i][j]], board[i][j], m, n)
                    visited[i][j] = False
        
        return ans
        
        
        