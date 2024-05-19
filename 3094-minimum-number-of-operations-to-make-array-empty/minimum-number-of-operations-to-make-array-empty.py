class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # Step 1: Build a frequency counter using Counter
        frequency_map = Counter(nums)
        count = 0

        # Step 2: Iterate through the frequency map
        for freq in frequency_map.values():
            # Check if a single element cannot be used in any operation
            if freq == 1:
                return -1

            # Step 3: Calculate the number of operations for the current element
            count += freq // 3

            # If there are remaining elements, add one more operation to the count
            if freq % 3 != 0:
                count += 1

        # Step 4: Return the total count, representing the minimum operations required
        return count