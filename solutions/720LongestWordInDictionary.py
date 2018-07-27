# hash table
# time: O(n * m)
# space: O(n)
class Solution:
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        words = set(words)
        ans = ''
        
        for word in words:
            if len(word) < len(ans) or len(word) == len(ans) and word > ans: continue
            if all([word[:i+1] in words for i in range(len(word))]):
                ans = word
                
        return ans

# Trie
# time: Build trie -- O(n * m)
#       Search -- O(n * m)   
# class TrieNode:
#     def __init__(self, c):
#         self.c = c
#         self.children = {}
#         self.is_word = False      

# class Trie:
#     def __init__(self):
#         self.root = TrieNode('')

#     def add(self, word):
#         node = self.root
#         for i in range(len(word)):
#             if word[i] not in node.children:
#                 node.children[word[i]] = TrieNode(word[i])
#             node = node.children[word[i]]
#         node.is_word = True     

#     def search(self, node, c):
#         if c in node.children and node.children[c].is_word:
#             return node.children[c]
#         else:
#             return None

# class Solution:
#     def longestWord(self, words):
#         """
#         :type words: List[str]
#         :rtype: str
#         """
#         ans = ''      

#         trie = Trie()
#         for word in words:
#             trie.add(word)

#         for word in words:
#             if len(word) < len(ans) or len(word) == len(ans) and word > ans: continue
#             node = trie.root
#             for i in range(len(word)):
#                 node = trie.search(node, word[i])
#                 if not node:
#                     break
#                 elif i == len(word) - 1:
#                     ans = word

#         return ans