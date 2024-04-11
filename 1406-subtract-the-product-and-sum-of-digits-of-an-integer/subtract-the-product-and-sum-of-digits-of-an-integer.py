class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product_d, sum_d = 1, 0
        for digit in str(n):
            product_d *= int(digit)
            sum_d += int(digit)
        return product_d - sum_d