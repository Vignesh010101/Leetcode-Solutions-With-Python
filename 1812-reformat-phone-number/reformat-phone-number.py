class Solution:
    def reformatNumber(self, number: str) -> str:
        number, a, i = (number.replace(' ', '').replace('-', '')), '', 0
        n = len(number)
        while n > 0:
            if n > 4 or n == 3:
                j = i + 3
                if j != len(number): a += number[i:j] + '-'
                else: a += number[i:j] 
                i = j
                n -= 3
            elif n == 4 or n == 2:
                j = i + 2
                if j != len(number): a += number[i:j] + '-'
                else: a += number[i:j] 
                i = j
                n -= 2
        return a