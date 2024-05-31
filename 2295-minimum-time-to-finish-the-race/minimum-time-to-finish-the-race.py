class Solution:
    def minimumFinishTime(self, tires: List[List[int]], changeTime: int, numLaps: int) -> int:
        
        bestlap = [float('inf') for i in range(numLaps+1)]
        
        for f,r in tires:
            cumLapTime = 0
            for lap in range(1,numLaps+1):
                
                nextLapTime = f*pow(r,lap-1)
                if nextLapTime > changeTime+bestlap[1]:
                    break
                    
                cumLapTime += nextLapTime
                bestlap[lap] = min(bestlap[lap],cumLapTime)
            
        @cache
        def dp(lapsleft):
            
            if lapsleft==0:
                return 0
            cur = float('inf')
            
            for lap in range(1,lapsleft+1):
                if bestlap[lap]==float('inf'):
                    break
                cur = min(cur, bestlap[lap] + dp(lapsleft-lap))
                
            return cur+changeTime
        return dp(numLaps)-changeTime
       