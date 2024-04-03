class Solution:
    def findComplement(self, num: int) -> int:
        # Convert num to binary string
        binary = bin(num)[2:]

        # Flip all bits in the binary string
        flipped_binary = ''.join(['0' if bit == '1' else '1' for bit in binary])

        # Convert the flipped binary string back to an integer
        if flipped_binary:
            return int(flipped_binary, 2)
        else:
            return 1