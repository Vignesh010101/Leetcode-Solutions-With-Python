class Solution:
    def smallestMissingValueSubtree(self, parents, nums):
        dict1 = defaultdict(int)

        def find(x):
            if x not in dict1:
                return x
            else:
                if x != dict1[x]:
                    dict1[x] = find(dict1[x])
                return dict1[x]

        def union(x,y):
            a,b = find(x),find(y)

            if a == b: return 0

            dict1[b] = a

            return a


        def dfs(tree):
            smallest = max({dfs(subtree) for subtree in graph[tree]}|{1})

            for subtree in graph[tree]:
                union(nums[tree],nums[subtree])

            for i in range(smallest,n+1):
                if find(i) != find(nums[tree]):
                    res[tree] = i
                    return i
            
            return i+1


        n, graph = len(nums), defaultdict(list)
        res = [1]*n

        for i,p in enumerate(parents):
            graph[p].append(i)

        res[0] = dfs(0)

        return res