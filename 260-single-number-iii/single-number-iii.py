class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        dict={}
        for num in nums:
            if num in dict:
                dict[num]+=1
            else:
                dict[num]=1

        result=[]
        for num, freq in dict.items():
            if freq==1:
                result.append(num)

        return result