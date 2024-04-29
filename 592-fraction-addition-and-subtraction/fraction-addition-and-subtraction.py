class Solution:
    def fractionAddition(self, expression: str) -> str:
        l = expression.split('+')

        num = []
        dum = []
        for i in l:
            temp = i.split('/')
            n= True

            for i in temp:
                if '-' in i and len(i)>2 and i.index('-')>0:
                    index = i.index('-')

                    dum.append(int(i[:index]))
                    num.append(int(i[index:]))
                    n=False
                else:
                    if n:
                        num.append(int(i))
                        n = False
                    else:
                        dum.append(int(i))
                        n=True
        d = reduce(math.lcm, dum)
        for i in range(len(num)):
            num[i] = num[i]*(d//abs(dum[i]))
        n = sum(num)
        return str(n//gcd(n,d))+"/"+str(d//gcd(n,d))