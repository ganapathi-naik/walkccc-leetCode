class Solution:
  def maxTotalFruits(
      self,
      fruits: list[list[int]],
      startPos: int,
      k: int,
  ) -> int:
    ans = 0
    maxRight = max(startPos, fruits[-1][0])
    amounts = [0] * (1 + maxRight)
    for position, amount in fruits:
      amounts[position] = amount
    prefix = [0] + list(itertools.accumulate(amounts))

    def getFruits(leftSteps: int, rightSteps: int) -> int:
      l = max(0, startPos - leftSteps)
      r = min(maxRight, startPos + rightSteps)
      return prefix[r + 1] - prefix[l]

    # Go right first.
    for rightSteps in range(min(maxRight - startPos, k) + 1):
      leftSteps = max(0, k - 2 * rightSteps)  # Turn left
      ans = max(ans, getFruits(leftSteps, rightSteps))

    # Go left first.
    for leftSteps in range(min(startPos, k) + 1):
      rightSteps = max(0, k - 2 * leftSteps)  # Turn right
      ans = max(ans, getFruits(leftSteps, rightSteps))

    return ans
