class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        n=len(bank)
        graph=[[] for _ in range(n+1)]
        # 0-> start , 1->bank[0] ,2->bank[1],....,n+1->end
        def check(s1,s2):
            c=0
            for i,j in zip(s1,s2):
                if i!=j:
                    c+=1
                    if c==2:
                        return False
            return True
        if end in bank:
            if check(start,end):
                # n+1->end
                graph[0].append(n+1)
                # graph[n+1].append(0)
        for i in range(n):
            if check(start,bank[i]):
                graph[0].append(i+1)
                graph[i+1].append(0)
            if (end in bank) and check(end,bank[i]):
                # graph[n+1].append(i+1)
                # n+1->end
                graph[i+1].append(n+1)
            for j in range(i+1,n):
                if check(bank[i],bank[j]):
                    graph[i+1].append(j+1)
                    graph[j+1].append(i+1)
        # print(graph)
        visited=set()
        def helper(ind):
            # n+1->end
            if ind==(n+1):
                return 0
            count=float("inf")
            visited.add(ind)
            for i in graph[ind]:
                if i not in visited:
                    count=min(count,1+helper(i))
            visited.remove(ind)
            return count
        x=helper(0)
        if x==float("inf"):
            return -1
        return x
        