import re
class Solution:
    def solveEquation(self, equation: str) -> str:
        first, second = equation.split('=')
        pattern = r"\+\d+x|-\d+x|\+x|-x|\d+x|x"
        lnf = re.findall(pattern, first)
        lns = re.findall(pattern, second)
        lnf.sort(key = lambda x: len(x), reverse=True)
        lns.sort(key = lambda x: len(x), reverse=True)
        for i in range(len(lnf)):
            first = first.replace(lnf[i], '')
            if re.search(r"\d+", lnf[i]) is not None:
                lnf[i] = lnf[i].replace('x','')
            else:
                lnf[i] = lnf[i].replace('x','1')
        for i in range(len(lns)):
            second = second.replace(lns[i], '')
            if re.search(r"\d+", lns[i]) is not None:
                lns[i] = lns[i].replace('x','')
            else:
                lns[i] = lns[i].replace('x','1')
        if first:
            first = eval(first)
        else:
            first = 0
        if second:
            second = eval(second)
        else:
            second = 0
        res1 = 0
        for i in lnf:
            res1 += int(i)
        res2 = 0
        for i in lns:
            res2 += int(i)
        res1 -= res2
        second -= first
        if res1 == 0:
            if second == 0:
                return "Infinite solutions"
            else:
                return "No solution"
            
        if res1 < 0:
            second *= -1
            res1 = abs(res1)
        if res1 == 1:
            return f"x={second}"
        elif res1 > 1 and second % res1 == 0:
            return f"x={second//res1}"
        else:
            return