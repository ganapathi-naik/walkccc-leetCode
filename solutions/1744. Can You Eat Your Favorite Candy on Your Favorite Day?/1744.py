class Solution:
  def canEat(self, candiesCount: list[int],
             queries: list[list[int]]) -> list[bool]:
    prefix = [0] + list(itertools.accumulate(candiesCount))
    return [prefix[t] // c <= d < prefix[t + 1] for t, d, c in queries]
