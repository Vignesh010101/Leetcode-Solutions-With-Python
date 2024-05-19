class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        ttl_sum=0
        cnt=0
        postv_min=float("inf")
        negtv_max=float("-inf")

        for nodeval in nums:
            new_nodeval=nodeval^k

            ttl_sum+=nodeval
            net_change=new_nodeval-nodeval

            if net_change>0:
                postv_min=min(postv_min, net_change)
                ttl_sum+=net_change
                cnt+=1
            else:
                negtv_max=max(negtv_max, net_change)

        if cnt % 2==0:
            return ttl_sum

        return max(ttl_sum-postv_min, ttl_sum+negtv_max)
