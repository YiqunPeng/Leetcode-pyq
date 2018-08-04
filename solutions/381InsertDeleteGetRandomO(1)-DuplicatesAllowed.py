from random import randint


class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.vals = []
        self.val2pos = collections.defaultdict(list)       

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        res = False if val in self.val2pos else True
        self.vals.append((val, len(self.val2pos[val])))
        self.val2pos[val].append(len(self.vals)-1)
        return res

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.val2pos:
            return False
        else:
            last = self.vals[-1]
            pos = self.val2pos[val][-1]
            self.vals[pos] = last
            self.val2pos[last[0]][last[1]] = pos
            
            self.val2pos[val].pop()
            self.vals.pop()
            
            if not self.val2pos[val]: del self.val2pos[val]
            return True
        
        
    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return self.vals[randint(0, len(self.vals) - 1)][0]


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()