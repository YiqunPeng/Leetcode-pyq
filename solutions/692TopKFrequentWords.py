from heapq import heappushpop, heappush, heappop

class Word:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq
        
    def __lt__(self, other):
        if self.freq == other.freq:
            return self.word > other.word
        else:
            return self.freq < other.freq
    
    def __eq__(self, other):
        return self.word == other.word and self.freq == other.freq
        

class Solution:
    # min heap, hash table
    # time: O(nlogk)
    # space: O(n)
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        freq = collections.defaultdict(int)
        for w in words:
            freq[w] += 1
        
        heap = []        
        for key, val in freq.items():
            n_word = Word(key, val)
            if len(heap) < k:
                heappush(heap, n_word)
            elif heap[0] < n_word:
                heappushpop(heap, n_word)
  
        ans = []
        while heap:
            ans.append(heappop(heap).word)
        return ans[::-1]
