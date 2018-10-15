class TreeNode:
    
    def __init__(self, char):
        self.c = char
        self.children = [None] * 26
        self.is_end = False
        
        
class Trie:
    
    def __init__(self):
        self.root = TreeNode('')
        
    
    def add_word(self, word):
        node = self.root
        for c in word:
            if not node.children[ord(c) - ord('a')]:
                node.children[ord(c) - ord('a')] = TreeNode(c)
            node = node.children[ord(c) - ord('a')]
        node.is_end = True
    
    
    def search_word(self, word):
        node = self.root
        for c in word:
            if not node.children[ord(c) - ord('a')]:
                return False
            node = node.children[ord(c) - ord('a')]
        return True if node.is_end else False


class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        memo = {}
        
        def dfs(s):
            if s in memo:
                return memo[s]
            
            res = []
            if not s:
                res.append('')
                return res
            
            for i in range(len(s)):
                if trie.search_word(s[:i+1]):
                    sub_list = dfs(s[i+1:])
                    for sub in sub_list:
                        if sub:
                            res.append(s[:i+1] + ' ' + sub)
                        else:
                            res.append(s[:i+1])
            
            memo[s] = res
            return res
                     
        
        trie = Trie()
        for word in wordDict:
            trie.add_word(word)
            
        return dfs(s)