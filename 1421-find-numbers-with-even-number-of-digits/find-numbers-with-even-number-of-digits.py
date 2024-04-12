class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        evenNumber = 0
        for num in nums:
            isEven = False
            while (num / 10 >= 1):
                isEven = not isEven
                num /= 10
            evenNumber += isEven
        return evenNumber 