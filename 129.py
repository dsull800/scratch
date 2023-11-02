# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode], current=0) -> int:
        if root is None:
            return 0

        value = 10 * current + root.val

        if root.left is None and root.right is None:
            return value
        else:
            return self.sumNumbers(root.left, value) + self.sumNumbers(root.right, value)


