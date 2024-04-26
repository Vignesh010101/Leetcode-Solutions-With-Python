class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        a,b=int(num1[:num1.index("+")]), int(num1[num1.index("+")+1:-1])
        c,d=int(num2[:num2.index("+")]), int(num2[num2.index("+")+1:-1])

        real_pt=a*c-b*d
        img_pt=a*d+b*c

        rslt=str(real_pt)+"+"+str(img_pt)+"i"
        return rslt