class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        temp = []
        first = 0
        last = k-1                 
        while (first <= len(s)-1):     
            if last > len(s)-1:
                last = len(s) - 1
            while(last >= first): 
                temp.append(s[last])  
                last = last - 1
            first = first + k                 
            last = first + (k-1)
            while(last >= first):
                if first > len(s)-1:
                    break
                temp.append(s[first])  
                first = first + 1                
            last = first + (k-1)       
        return ''.join(temp)
            