from random import randint


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val2pos = {}
        self.vals = []
        self.n = 0
        

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.val2pos:
            return False
        else:
            self.vals.append(val)
            self.val2pos[val] = self.n
            self.n += 1
            return True
            

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.val2pos:
            return False
        else:
            last = self.vals[self.n - 1]
            pos = self.val2pos[val]
            self.vals[pos] = last
            self.val2pos[last] = pos
            self.n -= 1
            self.vals.pop()
            del self.val2pos[val]
            return True
        

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return self.vals[randint(0, self.n - 1)]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()