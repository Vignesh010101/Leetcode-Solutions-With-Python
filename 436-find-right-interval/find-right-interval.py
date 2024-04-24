class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        j_st = sorted(enumerate(x[0] for x in intervals), key=lambda x: x[1])
        ret = []
        for x in intervals:
            k = bisect_left(j_st, x[1], key=lambda x: x[1])
            ret.append(j_st[k][0] if k < len(intervals) else -1)
        return ret