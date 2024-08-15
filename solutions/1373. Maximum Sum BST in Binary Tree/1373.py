class T:
  def __init__(self, isBST: bool = False,
               mx: int | None = None,
               mn: int | None = None,
               sum: int | None = None):
    self.isBST = isBST
    self.mx = mx
    self.mn = mn
    self.sum = sum


class Solution:
  def maxSumBST(self, root: TreeNode | None) -> int:
    self.ans = 0

    def traverse(root: TreeNode | None) -> T:
      if not root:
        return T(True, -math.inf, math.inf, 0)

      left: T = traverse(root.left)
      right: T = traverse(root.right)

      if not left.isBST or not right.isBST:
        return T()
      if root.val <= left.mx or root.val >= right.mn:
        return T()

      # The `root` is a valid BST.
      summ = root.val + left.sum + right.sum
      self.ans = max(self.ans, summ)
      return T(True, max(root.val, right.mx), min(root.val, left.mn), summ)

    traverse(root)
    return self.ans
