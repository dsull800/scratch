# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.min_val = 999999999
        self.vals = []

    def getMinimumDifference(self, root: Optional[TreeNode], first=True) -> int:
        if root is None:
            return None

        if root.left is not None:
            self.getMinimumDifference(root.left, False)

        self.vals.append(root.val)

        if root.right is not None:
            self.getMinimumDifference(root.right, False)

        if first:
            a = self.vals
            return min([x - a[i - 1] for i, x in enumerate(a)][1:])