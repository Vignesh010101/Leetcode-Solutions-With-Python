class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        exchange = {5:0, 10:0}
        for bill in bills:
            if bill == 5 : 
                exchange[5] +=1
            elif bill == 10 and exchange[5]: 
                exchange[10] +=1
                exchange[5] -= 1
            elif bill == 20 and ((exchange[5] and exchange[10]) or exchange[5] >=3):
                if exchange[5] and exchange[10]:
                    exchange[5] -= 1
                    exchange[10] -=1
                else: 
                    exchange[5] -=3
            else : return False
        return True
                