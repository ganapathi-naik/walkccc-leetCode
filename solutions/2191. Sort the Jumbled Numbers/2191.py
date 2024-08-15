class Solution:
  def sortJumbled(self, mapping: list[int], nums: list[int]) -> list[int]:
    def getMapped(num: int) -> int:
      mapped = []
      for c in str(num):
        mapped.append(str(mapping[ord(c) - ord('0')]))
      return int(''.join(mapped))
    A = [(getMapped(num), i, num) for i, num in enumerate(nums)]
    return [num for _, i, num in sorted(A)]
