class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        s=0
        prefix=0
        setd=set()
        for num in nums:
            s+=num
            d= s % k
            if d in setd:
                return True
            setd.add(prefix)
            prefix=d
        return False