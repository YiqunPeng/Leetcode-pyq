class TopVotedCandidate:

    def __init__(self, persons, times):
        """
        :type persons: List[int]
        :type times: List[int]
        """
        self.persons = persons
        self.times = times
        
        self.d = {}
        self.votes = collections.defaultdict(int)
        top = -1
        for i in range(len(persons)):
            self.votes[persons[i]] += 1
            if self.votes[persons[i]] >= top:
                top = self.votes[persons[i]]
                self.d[i] = persons[i]
            else:
                self.d[i] = self.d[i-1]
        
        
    def binary_search(self, t):
        if t >= self.times[-1]:
            return len(self.times) - 1
        
        l, r = 0, len(self.times) - 2
        while l <= r:
            m = l + (r - l) // 2
            if self.times[m] <= t < self.times[m+1]:
                return m
            elif self.times[m] > t:
                r = m - 1
            else:
                l = m + 1
        return r
        

    def q(self, t):
        """
        :type t: int
        :rtype: int
        """
        idx = self.binary_search(t)
        return self.d[idx]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)