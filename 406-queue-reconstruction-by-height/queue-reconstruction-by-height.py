class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        op=[]
        people.sort(key=lambda x: (-x[0], x[1]))
        for a in people:
            op.insert(a[1],a)

        return op