class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        l,r = 0,max(arr) 
        ans=0
        diff = float('inf')
        def arrsum(mid):
            sum=0
            for num in arr:
                sum += min(mid, num) 
            return sum

        while l <= r:
            mid = l+((r-l) // 2)  
            sum = arrsum(mid)           
            if abs(sum - target) < diff: 
                diff = abs(sum - target)
                ans = mid
            elif abs(sum - target) == diff: #In case of a tie, return the minimum such integer.
                ans = min(ans, mid)  
            if sum > target:
                r = mid - 1
            elif sum < target:
                l = mid + 1
            elif sum==target:
                return mid
            
        return ans