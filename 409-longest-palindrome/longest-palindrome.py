class Solution:
 def longestPalindrome(self, s:str)-> int:
    res=0
    count=collections.Counter(s)

    for c in count.values():
        res+=c if c % 2==0 else c-1
        
    haveoddcount = any(c %2 ==1 for c in count.values())
    return res+haveoddcount