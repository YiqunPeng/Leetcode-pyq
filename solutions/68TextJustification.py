class Solution:
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        def construct_line(line):            
            word_len = sum([len(w) for w in line])
            word_num = len(line)
            space_len = maxWidth - word_len
            
            res = line[0]
            
            if word_num > 1:
                div, mod = divmod(space_len, word_num - 1)
                res = line[0]
                for i in range(1, len(line)):
                    res = res + ' ' * div
                    if mod > 0:
                        res = res + ' '
                        mod -= 1
                    res = res + line[i]            
            else:
                res = res + ' ' * space_len
        
            return res
                
        
        def construct_lastline(line):
            res = line[0]
            for i in range(1, len(line)):
                res = res + ' ' + line[i]
            return res + ' ' * (maxWidth - len(res))
        
        
        ans = []
        
        curr_w = 0 
        line = []
        while words:
            if line and curr_w + len(words[0]) + 1 > maxWidth:
                ans.append(construct_line(line))
                line = []
                curr_w = 0
            else:
                word = words.pop(0)
                if not line:
                    curr_w = len(word)
                else:
                    curr_w += len(word) + 1
                line.append(word)
            if curr_w == maxWidth:
                ans.append(construct_line(line))
                line = []
                curr_w = 0
    
        if line:
            ans.append(construct_lastline(line))
            
        return ans
                
        