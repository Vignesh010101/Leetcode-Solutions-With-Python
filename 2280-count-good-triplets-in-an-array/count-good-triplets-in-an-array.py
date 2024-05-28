from sortedcontainers import SortedList

class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        mp = {x : i for i, x in enumerate(nums1)}
        sl = SortedList()
        ans = 0 
        for i, x in enumerate(nums2):
            x = mp[x]
            left = sl.bisect_left(x)
            right = (len(nums2)-1-x) - (len(sl)-left)
            ans += left * right
            sl.add(x)
        return ans