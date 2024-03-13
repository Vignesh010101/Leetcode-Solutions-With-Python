class Solution:
  def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
    base = minutesToTest // minutesToDie + 1
    rslt = 0
    x = 1
    while x < buckets:
      rslt += 1
      x *= base
    return rslt