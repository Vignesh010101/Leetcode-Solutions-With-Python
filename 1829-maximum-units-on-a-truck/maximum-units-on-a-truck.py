class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x:x[1],reverse = True)

        p=0
        for i, j in boxTypes:
            if i<truckSize:
                p+=i*j
                truckSize-=i
            else:
                p+=truckSize*j
                break
        return p            
        
       