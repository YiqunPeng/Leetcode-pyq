class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.num_dic = {}
        

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: void
        """
        self.num_dic[number] = self.num_dic.get(number, 0) + 1
        

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for key in self.num_dic:
            sub = value - key
            if sub == key and self.num_dic[key] > 1:
                return True
            elif sub != key and sub in self.num_dic:
                return True
        return False
                
        
# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)