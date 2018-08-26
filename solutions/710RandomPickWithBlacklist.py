class Solution:

    def __init__(self, N, blacklist):
        """
        :type N: int
        :type blacklist: List[int]
        """
        self.blacklist = set(blacklist)
        self.length = N - len(self.blacklist)
        
        self.remapping = {}
        j = self.length
        for b in self.blacklist:
            while j in self.blacklist:
                j += 1
            self.remapping[b] = j
            j += 1
        

    def pick(self):
        """
        :rtype: int
        """
        idx = random.randint(0, self.length - 1)
        
        return idx if idx not in self.blacklist else self.remapping[idx]


# Your Solution object will be instantiated and called as such:
# obj = Solution(N, blacklist)
# param_1 = obj.pick()