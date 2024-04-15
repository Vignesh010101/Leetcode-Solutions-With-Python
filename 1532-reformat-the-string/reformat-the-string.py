class Solution:
    def reformat(self, s: str) -> str:
        ls = list(s)
        digits = list(filter(lambda x : x.isdigit(), list(s)))
        letters = list(filter(lambda x : not x.isdigit(), list(s)))
        cd = len(digits)
        cl = len(letters)
        res = ""
        if abs(cd - cl) < 2 :
            for i in range(min(cd, cl)) :
                if cd > cl :
                    res += digits.pop() + letters.pop()
                else :
                    res += letters.pop() + digits.pop() 
            if digits :
                res += digits.pop() 
            if letters :
                res += letters.pop() 
            return res
        return ""