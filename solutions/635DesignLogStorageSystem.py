class LogSystem:

    def __init__(self):
        self.dic = {}
        self.gra = {'Year': 0, 'Month': 1, 'Day': 2, 'Hour': 3, 'Minute': 4, 'Second': 5}
        
    def process(self, timestamp):
        vals = timestamp.split(':')
        for i in range(len(vals)):
            if vals[i][0] == '0':
                vals[i] = vals[i][1]
            vals[i] = int(vals[i])
        return vals
        
    def put(self, id, timestamp):
        """
        :type id: int
        :type timestamp: str
        :rtype: void
        """
        self.dic[id] = self.process(timestamp)
        

    def retrieve(self, s, e, gra):
        """
        :type s: str
        :type e: str
        :type gra: str
        :rtype: List[int]
        """
        res = []
        
        g = self.gra[gra]
        s = self.process(s)
        e = self.process(e)
        
        for key, val in self.dic.items():
            start, end = False, False
            flag = True
            for i in range(g+1):
                if s[i] < val[i] < e[i]:
                    start, end = True, True
                    flag = True
                    break
                if val[i] < e[i]:
                    end = True
                if val[i] > s[i]:
                    start = True
                if not start and val[i] < s[i] or not end and val[i] > e[i]:
                    flag = False
                    break
            if flag: res.append(key)
    
        return res


# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(s,e,gra)