class Solution:
    def frequencySort(self, s: str) -> str:
        #ord('0')=48
        freq=[0]*75
        for c in s:
            freq[ord(c)-48]+=1
        freq_c=[]
        for i in range(75):
            if freq[i]==0: continue
            freq_c.append([freq[i], chr(48+i)])
        freq_c.sort(reverse=True)
        ans=""
        for n, c in freq_c:
            ans+=c*n
        return ans