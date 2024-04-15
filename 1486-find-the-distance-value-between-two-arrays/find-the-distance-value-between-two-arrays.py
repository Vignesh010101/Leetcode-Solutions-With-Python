class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        res, buckets = 0, dict() # (minVa, maxVal)
        
        def getKey(val):
            return val // d
        
        def addVal(val):
            key = getKey(val)
            #save only min and max value in bucket, others values not
            if key in buckets:
                if buckets[key][0] > val: buckets[key][0] = val
                elif buckets[key][1] < val: buckets[key][1] = val
            else:
                buckets[key] = [val, val]
        
        #initialize buckets     
        for val in arr2: addVal(val)

        for val in arr1:
            key = getKey(val)
            if key in buckets: continue #in one bucket all values x < d
            #check sibling buckets
            if key - 1 in buckets and val - buckets[key-1][1] <= d: continue #maxVal from the left side is nearest
            if key + 1 in buckets and buckets[key+1][0] - val <= d: continue #minVal from the right side is nearest
            res += 1

        return res