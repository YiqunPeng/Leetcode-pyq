# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        def recursion(n_list):
            for item in n_list:
                if item.isInteger():
                    self.list.append(item.getInteger())
                else:
                    recursion(item.getList())
                 
        self.list = []
        recursion(nestedList)
        self.pos = 0
        self.len = len(self.list)
        

    def next(self):
        """
        :rtype: int
        """
        val = self.list[self.pos]
        self.pos += 1
        return val
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.pos < self.len
        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())