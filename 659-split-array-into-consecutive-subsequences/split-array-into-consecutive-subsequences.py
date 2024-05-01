from collections import Counter as counter #library for making frequency of numbers of list
class Solution:
    def isPossible(self, nums: List[int]) -> bool: 
        #make frequency of list nums
        f=counter(nums)
        print(f) 
        #create dictionary for storing frequency of last numbers of subsequence
        m=counter()
        #loop for nums's numbers
        for i in nums:
            #if frequency of any number becomes 0 then skip
            if f[i]==0:
                continue 
            #if just previous number of last number of any subsequence present
            #in m(not having freq 0 means m[i-1]>0) then it can be appended in any existing 
            #subsequence , example is nums= [1,2,3,3,4,4,5,5] 
            #if make [1,2,3],[3,4,5],[4,5] this will return false but that should be true 
            #so this below condition will help to join [1,2,3],[4,5] = [1,2,3,4,5]
            if m[i-1]>0:
                f[i]-=1
                m[i]+=1
                m[i-1]-=1
            # initially making subsequence of length 3 so checking three consecutive numbers
            # i.e , f[i] , f[i+1] , f[i+2]
            elif f[i]>0 and f[i+1]>0 and f[i+2]>0: 
                #after amking of subsequence decrement the frequency of those numbers
                #because they are already used in subsequence
                f[i]-=1
                f[i+1]-=1
                f[i+2]-=1
                m[i+2]+=1
            #if above conditions dont satisfy then return false
            else:
                return False
        #if everything will go conditionally (or not false) then return true
        print(m)
        return True
        