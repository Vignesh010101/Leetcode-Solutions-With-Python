class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l1 = []
        l2 = []
        for num in nums:
            if num%2==0:
                l1.append(num)
            else:
                l2.append(num)
        return l1 + l2