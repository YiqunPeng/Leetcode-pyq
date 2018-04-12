class MyCalendar:

    def __init__(self):
        self.calendar = []
        

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        for event in self.calendar:
            if start < event[1] and end > event[0]:
                return False
        
        self.calendar.append([start, end])
        return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)