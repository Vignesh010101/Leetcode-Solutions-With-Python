class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtracking(start, route):
            result_list.append(route)
            for i in range(start, len(nums)):
                backtracking(i+1, route + [nums[i]])
            
        result_list=[]
        backtracking(0,[])
        return result_list