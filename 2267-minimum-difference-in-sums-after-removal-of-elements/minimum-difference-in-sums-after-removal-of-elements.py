import heapq
class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 3
        A, B = sorted([-v for v in nums[:n]]), sorted(nums[-n:]), 
        possible_A, possible_B = [-sum(A)], [sum(B)]
        for i in range(n, 2*n):
            heapq.heappush(A, -nums[i])
            possible_A.append(possible_A[-1] + nums[i] + heapq.heappop(A))
            heapq.heappush(B, nums[-i-1])
            possible_B.append(possible_B[-1] + nums[-i-1] - heapq.heappop(B))
        return min(a - b for a, b in zip(possible_A, possible_B[::-1]))