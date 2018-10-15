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
        def dfs(nestedList):
            res = []
            if not nestedList: return res
            for nested_integer in nestedList:
                if nested_integer.isInteger():
                    res.append(nested_integer.getInteger())
                else:
                    res.extend(dfs(nested_integer.getList()))
            return res
        
        self.flatted = dfs(nestedList)
        self.idx = 0
            

    def next(self):
        """
        :rtype: int
        """
        res = self.flatted[self.idx]
        self.idx += 1
        return res
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.idx < len(self.flatted)
        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())