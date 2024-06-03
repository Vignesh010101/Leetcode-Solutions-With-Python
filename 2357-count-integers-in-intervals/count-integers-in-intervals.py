from sortedcontainers import SortedList

class CountIntervals:

    def __init__(self):
        self.cov = 0 
        self.interv = SortedList([(-inf, -inf), (inf, inf)])

    def add(self, left: int, right: int) -> None:
        li = self.interv.bisect_left((left - 1, -inf))
        if self.interv[li - 1][1] >= left - 1:
            li -= 1
        lval = min(self.interv[li][0], left)
        ri = self.interv.bisect_right((right + 1, inf))
        rval = max(self.interv[ri - 1][1], right)
        
        
        to_delete = 0
        for _ in range(li, ri):
            to_delete += self.interv[_][1] - self.interv[_][0] + 1
        self.cov += rval - lval + 1 - to_delete
        del self.interv[li: ri]
        self.interv.add((lval, rval))

    def count(self) -> int:
        return self.cov        


# Your CountIntervals object will be instantiated and called as such:
# obj = CountIntervals()
# obj.add(left,right)
# param_2 = obj.count()