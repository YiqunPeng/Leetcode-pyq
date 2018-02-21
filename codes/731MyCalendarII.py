class MyCalendarTwo:

    def __init__(self):
        self.books = []
        self.overlaps = []
        

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        def is_overlapped(book1, book2):
            if book2[0] < book1[1] and book2[1] > book1[0]:
                return True
            else:
                return False
        
        def update_overlaps(s, e):
            for book in self.books:
                if is_overlapped(book, [s,e]):
                    self.overlaps.append([max(s,book[0]), min(e,book[1])])

     
        for overlap in self.overlaps:
            if is_overlapped(overlap, [start, end]):
                return False
            
        update_overlaps(start, end)
        self.books.append([start, end])
        return True
        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)