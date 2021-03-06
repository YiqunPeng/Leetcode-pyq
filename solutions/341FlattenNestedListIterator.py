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
        self.stack = []
        for n_int in nestedList[::-1]:
            if n_int.isInteger() or n_int.getList():
                self.stack.append(n_int)
        

    def next(self):
        """
        :rtype: int
        """
        return self.stack.pop().getInteger()


    def hasNext(self):
        """
        :rtype: bool
        """
        if len(self.stack) == 0: return False
        
        top = self.stack[-1]
        if top.isInteger():
            return True
        else:
            while not top.isInteger():
                li = top.getList()
                self.stack.pop()
                for n_int in li[::-1]:
                    if n_int.isInteger() or n_int.getList(): 
                        self.stack.append(n_int)
                if len(self.stack) == 0: return False 
                top = self.stack[-1]
        
        return len(self.stack) != 0
        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())