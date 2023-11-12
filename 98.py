# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.prev = -99999999999

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None or root.val is None:
            return True

        left = self.isValidBST(root.left)
        if self.prev >= root.val:
            return False
        self.prev = root.val
        right = self.isValidBST(root.right)
        return right and left