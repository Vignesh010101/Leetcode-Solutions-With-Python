class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.index = [i for i in range(0,len(nums))]

    def reset(self) -> List[int]:
        n = len(self.nums)
        nums2 = [0 for _ in range(0,n) ]
        for i in range(0,n):
            nums2[self.index[i]] = self.nums[i]
        self.index = [i for i in range(0,n)]
        self.nums = nums2
        return self.nums

    def shuffle(self) -> List[int]:
        n = len(self.nums)
        nums2 = [ 0 for _ in range(0,n) ]
        index2 = [0 for _ in range(0,n) ]
        filled = []
        i = 0
        while(i < n):
            r = randint( 0,n-1)
            if( r not in filled):
                filled.append(r);
                nums2[r]  =  self.nums[i]
                index2[r] = self.index[i] 
                i+=1
        self.nums = nums2 ;
        self.index = index2 
        return self.nums
        

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()