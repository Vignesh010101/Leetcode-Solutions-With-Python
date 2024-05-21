class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        tasks.sort()
        workers.sort()
        
        def fn(k, p=pills): 
            """Return True if k tasks can be completed."""
            ww = workers[-k:]
            for t in reversed(tasks[:k]): 
                if t <= ww[-1]: ww.pop()
                elif t <= ww[-1] + strength and p: 
                    p -= 1
                    i = bisect_left(ww, t - strength)
                    ww.pop(i)
                else: return False 
            return True 
          
        lo, hi = 0, min(len(tasks), len(workers))
        while lo < hi: 
            mid = lo + hi + 1 >> 1
            if fn(mid): lo = mid
            else: hi = mid - 1
        return lo 