import random


class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sums = []
        prefix_sum = 0
        for i in range(len(w)):
            prefix_sum += w[i]
            self.prefix_sums.append(prefix_sum)
        self.total_sum = prefix_sum

    def pickIndex_v1(self) -> int:
        # float number
        random_number = self.total_sum * random.random() # half-open range 0.0 <= X < 1.0
        left, right = 0, len(self.prefix_sums) - 1
        while left < right:
            mid = (left + right) // 2
            if random_number > self.prefix_sums[mid]:
                left = mid + 1
            else:
                right = mid
        return left

    def pickIndex(self) -> int:
        random_number = self.total_sum * random.random()
        for i in range(len(self.prefix_sums)):
            if random_number < self.prefix_sums[i]:
                return i



# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()



# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()