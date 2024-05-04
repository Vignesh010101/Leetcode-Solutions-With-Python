class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l,r=0,len(people)-1
        x=0
        while l<=r:
            x+=1
            if people[l]+people[r]<=limit:
                l+=1
            r-=1

        return x

        