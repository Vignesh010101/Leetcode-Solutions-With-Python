from datetime import datetime as dt
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        date1 = date1.split('-')
        date2 = date2.split('-')
        date1 = [int(i) for i in date1]
        date2 = [int(i) for i in date2]
        m = dt(date1[0], date1[1], date1[2])
        n = dt(date2[0], date2[1], date2[2])
        return abs((n-m).days)