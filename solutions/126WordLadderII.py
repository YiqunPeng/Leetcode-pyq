class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """    
        word_dic = {key : set() for key in wordList} 
        word_dis = {key : sys.maxsize for key in wordList}
        visited = set()
        used = set()
        q = collections.deque([])
        ans = []        
        if endWord not in word_dic: 
            return []
                

        def add_next_words(word, dis):
            if word == endWord: return 0
            is_end = False
            has_next = False

            cnt = 0
            for i in range(len(beginWord)):
                for c in string.ascii_lowercase:
                    if c == word[i]: continue
                    next_word = word[:i] + c + word[i+1:]            
                    if next_word in word_dic.keys():
                        has_next = True
                        if word not in word_dic[next_word] and dis < word_dis[next_word]:
                            word_dic[next_word].add(word)
                        if next_word not in visited:
                            # cnt += 1
                            q.append((next_word, dis+1))
                            visited.add(next_word)
                            word_dis[next_word] = dis + 1

                    if next_word == endWord:
                        is_end = True
            
            if not has_next:
                if word in used: used.remove(word)
            else:
                used.add(word)
  
            return dis+1 if is_end else 0
                        
        min_dis = sys.maxsize
        if add_next_words(beginWord, 1) == 2:
            min_dis = 2
           
        while q:
            word, dis = q.popleft()
            
            if dis > min_dis: break 
            
            res = add_next_words(word, dis)
            if res: 
                min_dis = min(res, min_dis)

        
        def dfs(word_seq, min_dis):
            if word_seq[0] == beginWord and len(word_seq) == min_dis:
                ans.append(word_seq)
                return
            if word_seq[0] not in word_dic or not word_dic[word_seq[0]]:
                return
            for word in word_dic[word_seq[0]]:
                if word in used and word not in word_seq:
                    used.remove(word)
                    dfs([word] + word_seq, min_dis)
                    used.add(word)
            
        
        for word in word_dic[endWord]:
            if word in used:
                used.remove(word)
                dfs([word, endWord], min_dis)
                used.add(word)
        
        return ans
            