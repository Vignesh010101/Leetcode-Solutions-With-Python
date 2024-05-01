class Solution:
  def constructArray(self, n: int, k: int) -> List[int]:
    ans = list(range(1, n - k + 1))
    for i in range(k):
        diff = i // 2 + 1
        if i % 2 == 0:
            ans.append(n - diff + 1)
        else:
            ans.append(n - k + diff)

    return ans