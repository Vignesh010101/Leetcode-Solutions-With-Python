class Solution:
    def dayOfYear(self, date: str) -> int:
        y,m,d = map(int, date.split('-'))
        if (y%400==0 or (y%100!=0 and y%4==0)) and m>2: d+=1
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        for i in range(1, m):
            d+=months[i-1]
        return d
        