class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        n=len(distance)
        if start>destination:
            start,destination=destination,start
        distance=distance + distance
        dist1=sum(distance[start:destination])
        dist2=sum(distance[destination:start+n])
        return min(dist1,dist2)
       
        