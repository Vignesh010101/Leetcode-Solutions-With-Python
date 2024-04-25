class Solution:
    def find132pattern(self, nums: List[int]) -> bool:


        #  this is an example of monotonic stack ds
        # this actually maintains either decreasing or increasing elements in a stack
        # consider last 2 positions if the 
        # consider eg ::    1 5 0 3 4
        '''
            initially 4 in stack
            the since 3<4 3 will add then 0 will add into the stack
            now 5 since 5>0 pop all elements that are less than the 5 
            and update the mini2 as the max element that is popped out

            after this operation 
            mini2 = 4
            in stack is 5 

            the next num which is less than mini2 will form the series
            here   1 --> 5 --> 4 will form the patten

        '''

        n = len(nums)
        st = []
        mini2 = float('-inf')

        for i in range(n-1,-1,-1):
            if i==n-1:
                st.append(nums[i])
            if nums[i] < mini2 :
                return True
            if nums[i]<st[-1] :
                st.append(nums[i])
            elif nums[i]>st[-1] :
                c = 0
                while(len(st)>0 and nums[i] > st[-1]) :
                    mini2 = st[-1]
                    st.pop()                    
                st.append(nums[i])

        return False

        