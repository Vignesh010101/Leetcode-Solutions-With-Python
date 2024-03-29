class Solution:
  def minimumOneBitOperations(self, n: int) -> int:
    if n == 0:
      return 0
    x = 1 << n.bit_length() - 1
    return self.minimumOneBitOperations(n ^ (x | x >> 1)) + 1 + x - 1