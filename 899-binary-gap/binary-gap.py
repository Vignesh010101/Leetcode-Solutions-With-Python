class Solution:
    def binaryGap(self, n: int) -> int:
        binary = bin(n)
        binary= binary[2:]
        found = False
        max_count =0
        for i in range(len(binary)):
             if(binary[i]=='1' and found ==False):
                 start= i
                 found = True
             elif(binary[i]=='1' and found==True):
                 count = i- start
                 start= i
                 if(count>max_count):
                     max_count= count
        return max_count

             