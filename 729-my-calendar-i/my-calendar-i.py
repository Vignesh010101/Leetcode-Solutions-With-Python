class MyCalendar:

    def __init__(self):
        self.booked = []

    def book(self, start: int, end: int) -> bool:
        if self.check_booking(start, end):
            self.booked.append([start, end])
            return True
        return False
        
    # to check -> new booking is valid or not
    def check_booking(self, start, end):
        for x, y in self.booked:
            
            # invalid if start in [x, y-1] or end in  [x+1, y]
            if (start >= x and start < y) or (end > x and end <= y):    
                return False
            
            # invalid if already booked period is within the new booking
            if x > start and y < end:
                return False
        return True
               


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)