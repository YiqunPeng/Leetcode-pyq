class Node:
    
    def __init__(self, val = None, is_end = False):
        self.val = val
        self.children = [None] * 26
        self.is_end = is_end
    
    
class Solution:
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        def add_word(word):
            root = trie
            for c in word:
                if not root.children[ord(c) - ord('a')]:
                    root.children[ord(c) - ord('a')] = Node(c)
                root = root.children[ord(c) - ord('a')]
            root.is_end = True
            
            
        def find_palindrome_path(p_paths, root, curr):
            if root.is_end and is_palindrome(curr):
                p_paths.append(curr)
                
            for child in root.children:
                if child: find_palindrome_path(p_paths, child, curr + child.val)
        
        
        def search_word(word):
            root = trie
            res = []
            for i, c in enumerate(word):
                if not root: break
                if root.is_end:
                    if is_palindrome(word[i:]):
                        res.append(words_dict[word[:i][::-1]])
                root = root.children[ord(c) - ord('a')]
            if root:
                p_paths = []
                find_palindrome_path(p_paths, root, '')
                for path in p_paths:
                    res.append(words_dict[path[::-1] + word[::-1]])
            return res         
                    
        
        def is_palindrome(s):
            if s in palindrome_dict: return palindrome_dict[s]
            l, r = 0, len(s) - 1
            while l < r:
                if s[l] != s[r]: 
                    palindrome_dict[s] = False
                    return False
                l += 1
                r -= 1
            palindrome_dict[s] = True
            return True
        
  
        palindrome_dict = {}
        words_dict = {}
        trie = Node()
        for i, word in enumerate(words):
            add_word(word[::-1])
            words_dict[word] = i
            
        ans = []
        n = len(words)
        for i in range(n):
            res = search_word(words[i])
            for j in res:
                if i != j: ans.append([i, j])
        return ans       