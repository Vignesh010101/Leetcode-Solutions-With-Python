class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        # Initialize an empty list to store the target array
        target = []
        # Iterate through each element in the input lists
        for i in range(len(nums)):
            # Check if the index value matches the current length of the target list
            if index[i] == len(target):
                # If the index is at the end, simply append the current number to the target
                target.append(nums[i])
            else:
                # If the index is not at the end, insert the current number at the specified index
                # This is done by slicing the target list and inserting the number in the middle
                target = target[:index[i]] + [nums[i]] + target[index[i]:]
        # Return the final target array
        return target