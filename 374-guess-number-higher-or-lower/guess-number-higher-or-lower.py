# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        rng1=1
        rng2=n

        while rng1<=rng2:
            mid=(rng1+rng2)//2
            check=guess(mid)
            if check==0:
                return mid
            elif check==-1:
                rng2=mid-1
            else:
                rng1=mid+1
        
        return int(mid)