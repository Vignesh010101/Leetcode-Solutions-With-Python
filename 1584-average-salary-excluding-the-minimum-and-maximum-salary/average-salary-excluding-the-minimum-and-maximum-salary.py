class Solution:
    def average(self, salary: List[int]) -> float:
        salary=sorted(salary)
        result=[]
        for i in range(1,len(salary)-1):
            result.append(salary[i])
        return sum(result)/len(result)