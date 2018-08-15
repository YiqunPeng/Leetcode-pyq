class Solution:
    def __init__(self):
        self.ans = []
    
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        ticket_dict = collections.defaultdict(list)
        airport_dict = collections.defaultdict(int)
        for t in tickets:
            ticket_dict[t[0]].append(t[1])
            airport_dict[t[0]+t[1]] += 1
        for key in ticket_dict:
            ticket_dict[key].sort()
        
        def dfs(res):
            if self.ans: return
            if len(res) == len(tickets) + 1:
                self.ans = res[:]
                return 
            
            airports = list(ticket_dict[res[-1]])
            for i, airport in enumerate(airports):
                if airport_dict[res[-1]+airport] > 0:
                    airport_dict[res[-1]+airport] -= 1
                    dfs(res + [airport])
                    airport_dict[res[-1]+airport] += 1  

        dfs(['JFK'])
        return self.ans
             