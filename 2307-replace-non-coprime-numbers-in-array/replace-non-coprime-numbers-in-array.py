from math import lcm,gcd
class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack=[]
        
        for num in nums:
            top=num
            while stack and gcd(top, stack[-1])>1:
                top=lcm(stack[-1], top)
                stack.pop()

            stack.append(top)

        return stack