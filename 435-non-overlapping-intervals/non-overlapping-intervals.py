class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        res=0
        prev=intervals[0]
        for interval in intervals:
            if interval[0]<prev[1]:
                res+=1
            else:
                prev=interval
        return res-1