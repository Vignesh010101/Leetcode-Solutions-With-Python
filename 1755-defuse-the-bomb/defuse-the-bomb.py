class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        ind = 0
        li = [0 for i in range(len(code))]
        if k>0:
            for j in range(len(code)):
                sum = 0
                ind = j
                for i in range(k):
                    if ind+1 >= len(code):
                        sum += code[(ind+1)%len(code)]
                    else:
                        sum += code[ind+1]
                    ind += 1
                li[j] = sum
        elif k<0:
            r = -k
            for j in range(len(code)):
                sum = 0
                ind = j
                for i in range(r):
                    if ind-1 <0:
                        sum += code[ind-1]
                        ind -= 1
                    else:
                        sum += code[ind-1]
                        ind -= 1
                li[j] = sum
        return li

