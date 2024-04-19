class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        
        q = deque([0])
        seen = set()
        steps = [jug1Capacity, -jug1Capacity, jug2Capacity, -jug2Capacity]

        while q:
            cur = q.popleft()
            for step in steps:
                tot = cur + step 
                if tot == targetCapacity:
                    return True
                if tot not in seen and 0 <= tot <= jug1Capacity + jug2Capacity:
                    seen.add(tot)
                    q.append(tot)
        return False