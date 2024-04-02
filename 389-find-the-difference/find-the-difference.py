class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dict={}
        #count chrctrs in str t
        for c in t:
            dict[c]=dict.get(c,0)+1
        
        #remove counts for chrctrs in str s
        for c in s:
            dict[c]-=1
            if dict[c]==0:
                del dict[c]

        #return the dictionary with differences
        return list(dict.keys())[0]