# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.peeking_iterator = iterator
        self.peek_flag = False
        self.peek_val = 0
        

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.peek_flag:
            return self.peek_val
        else:
            self.peek_flag = True
            self.peek_val = self.peeking_iterator.next()
            return self.peek_val
        

    def next(self):
        """
        :rtype: int
        """
        if self.peek_flag:
            self.peek_flag = False
            return self.peek_val
        else:
            return self.peeking_iterator.next()
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.peeking_iterator.hasNext() or self.peek_flag
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].