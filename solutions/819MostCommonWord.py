class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        paragraph = re.sub(r'[^a-zA-Z]', ' ', paragraph).lower()
        words = paragraph.split()
        banned = set(banned)        
        counter = collections.defaultdict(int)
        
        ans = None
        max_count = 0
        for word in words:
            if word in banned: continue
            counter[word] += 1
            if max_count < counter[word]:
                max_count = counter[word]
                ans = word
        
        return ans