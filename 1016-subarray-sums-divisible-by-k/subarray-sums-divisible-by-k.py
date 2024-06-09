class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        visited=defaultdict(int)
        visited[0]=1
        curr_sum=result=0

        for num in nums:
            curr_sum+=num
            remainder=curr_sum % k
            result+=visited[remainder]
            visited[remainder]+=1

        return result