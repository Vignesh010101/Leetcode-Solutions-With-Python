class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        self.avail = {}
        self.price = {}
        self.movies = defaultdict(list)
        for s, m, p in entries: 
            heappush(self.movies[m], (p, s))
            self.avail[s, m] = True # unrented 
            self.price[s, m] = p
        self.rented = []
        

    def search(self, movie: int) -> List[int]:
        if movie not in self.movies: return []
        ans, temp = [], []
        while len(ans) < 5 and self.movies[movie]: 
            p, s = heappop(self.movies[movie])
            temp.append((p, s))
            if self.avail[s, movie]: ans.append((p, s))
        for p, s in temp: heappush(self.movies[movie], (p, s))
        return [x for _, x in ans]
            

    def rent(self, shop: int, movie: int) -> None:
        self.avail[shop, movie] = False
        p = self.price[shop, movie]
        heappush(self.rented, (p, shop, movie))
        

    def drop(self, shop: int, movie: int) -> None:
        self.avail[shop, movie] = True 
        

    def report(self) -> List[List[int]]:
        ans = []
        while len(ans) < 5 and self.rented: 
            p, s, m = heappop(self.rented)
            if not self.avail[s, m] and (not ans or ans[-1] != (p, s, m)): 
                ans.append((p, s, m))
        for p, s, m in ans: heappush(self.rented, (p, s, m))
        return [[s, m] for _, s, m in ans]


# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()