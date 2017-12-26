class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {}
        

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        self.dic[key] = val
            

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        ans = 0
        for (key, val) in self.dic.items():
            if key.startswith(prefix):
                ans += val
        return ans


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)