class BookMyShow(object):

    def __init__(self, n, m):
        self.calls_remaining = int(5 * 10e4)
        n = min(n, self.calls_remaining)
        m = min(m, 10e9)
        
        self.n, self.m = n, m
        self.rows = {i: m for i in range(n)}
        self.last_row_f = 0
        self.dbook = {m: 0}
        self.places_rem = m * n
        self.cache = {}

    def gather(self, k, maxRow):
        if not self.calls_remaining or k > self.m or k > self.places_rem: 
            return []
        self.calls_remaining -= 1
        maxRow = maxRow if maxRow < self.n else self.n - 1

        i = self.dbook.get(k, self.last_row_f)
        while i <= maxRow:
            if self.rows.get(i, 0) >= k:
                seat = self.m - self.rows[i]
                self.rows[i] -= k
                if self.rows[i] == self.m:
                    self.last_row_f = i
                self.dbook[k] = i
                self.places_rem -= k
                return [i, seat]
            i += 1

        self.dbook[k] = maxRow
        return []

    def scatter(self, k, maxRow):
        if not self.calls_remaining or k > self.places_rem: 
            return False
        self.calls_remaining -= 1
        k = k if k < 10e9 else int(10e9)
        maxRow = maxRow if maxRow < self.n else self.n - 1

        if self.cache.get(maxRow, float('inf')) <= k: 
            return False

        free_space_taken = 0
        i = self.last_row_f
        while i <= maxRow:
            nb_free = self.rows.get(i, 0)
            if nb_free:
                if nb_free >= k:
                    self.rows[i] -= k
                    self.places_rem -= k
                    j = self.last_row_f
                    while j < i:
                        self.places_rem -= self.rows.pop(j, 0)
                        j += 1
                    self.last_row_f = j
                    return True
                k -= nb_free
            free_space_taken += 1
            i += 1

        self.cache[maxRow] = k
        return False

# Your BookMyShow object will be instantiated and called as such:
# obj = BookMyShow(n, m)
# param_1 = obj.gather(k,maxRow)
# param_2 = obj.scatter(k,maxRow)