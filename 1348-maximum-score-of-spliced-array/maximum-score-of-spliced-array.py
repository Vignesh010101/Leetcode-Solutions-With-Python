class Solution:
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        t1 = t2 = 0
        mx1 = mx2 = 0
        for i in range(len(nums1)):
            t1 += nums2[i]-nums1[i]
            t2 += nums1[i]-nums2[i]
            mx1 = max(t1, mx1)
            mx2 = max(t2, mx2)
            if t1 < 0: t1 = 0
            if t2 < 0: t2 = 0
        return max(sum(nums1)+mx1, sum(nums2)+mx2)