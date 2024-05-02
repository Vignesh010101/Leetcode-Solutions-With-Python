class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        nums1, nums2 = "".join(map(chr, nums1)), "".join(map(chr, nums2))

        def has_subarray(n):
            seen = {nums1[i:i + n] for i in range(len(nums1) - n + 1)}
            return any(nums2[i:i + n] in seen for i in range(len(nums2) - n + 1))

        lo, hi = 0, min(len(nums1), len(nums2))
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if has_subarray(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo