# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
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

class Solution:
    def depthSumInverse(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        def find_max_depth(nestedList, d):
            res = d
            print(nestedList)
            for i in nestedList:
                if i.isInteger():
                    continue
                else:
                    res = max(res, find_max_depth(i.getList(), d+1))
            return res
        
        
        def sum_value(nestedList, depth):
            ans = 0
            for i in nestedList:
                if i.isInteger():
                    ans += i.getInteger() * depth
                else:
                    ans += sum_value(i.getList(), depth-1)
            return ans
            
        
        if not nestedList: return 0
        
        max_depth = find_max_depth(nestedList, 1)        
        return sum_value(nestedList, max_depth)

                