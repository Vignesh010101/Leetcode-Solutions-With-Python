class Solution:
  def leastInterval(self, tasks: List[str], n: int) -> int:
    count = collections.Counter(tasks)
    maxFreq = max(count.values())
    maxFreqTaskOccupy = (maxFreq - 1) * (n + 1)

    nMaxFreq = sum(value == maxFreq for value in count.values())
    return max(maxFreqTaskOccupy + nMaxFreq, len(tasks))