class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n_a = Counter(nums1)
        n_b = Counter(nums2)
        res = []
        for k, v in n_b.items():
            if k in n_a:
                res.extend([k] * min(v, n_a[k]))
        return res