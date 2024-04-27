class Solution:
    def jump(self, nums: List[int]) -> int:
        start=0
        end=0
        reaching=0

        for i in range(len(nums)-1):
            reaching=max(reaching, i+nums[i])
            if reaching>=len(nums)-1:
                start+=1
                break
            if i==end:
                start+=1
                end=reaching
            
        return start