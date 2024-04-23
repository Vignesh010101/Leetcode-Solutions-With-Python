class Solution:
    def findNthDigit(self, n: int) -> int:
        # Initialize digit length (dl) to 1 for numbers 1-9, and count (c) of such numbers to 9
        dl, c = 1, 9
        
        # Loop to find the length of the number containing the nth digit
        while n > dl * c:
            n -= dl * c  # Subtract the digits counted so far
            dl += 1      # Increase digit length as we move to the next group (e.g., from 9 to 10, 99 to 100)
            c *= 10      # Increase the count for the next group of numbers
        
        # Calculate the start of the numbers with current digit length (dl)
        start = 10 ** (dl - 1)
        
        # Find the actual number that contains the nth digit
        num = start + (n - 1) // dl
        
        # Find the position of the nth digit in the number
        di = (n - 1) % dl
        
        # Extract and return the nth digit
        return int(str(num)[di])