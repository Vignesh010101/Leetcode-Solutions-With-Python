class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        res = []
        self.parent = list(range(n))
        for a,b in requests:
            temp = self.parent.copy()
            self.union(a,b)
            flag = True
            for x,y in restrictions:
                if self.find(x)==self.find(y):
                    flag = False
                    break
            if flag:
                res.append(True)
            else:
                res.append(False)
                self.parent = temp
        
        return res

    def find(self, a):
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a
        
    def union(self, a, b):
        self.parent[self.find(b)] = self.find(a)