# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode], right_half = None, depth = 0) -> bool:
        if depth == 0:
            if root:
                right_half = root.right
                root = root.left
            else:
                return True

        if right_half == root == None:
            return True
        elif (right_half is None or root is None) and right_half != root:
            return False
        else:
            root_left, root_right = root, right_half
            if root_left.val != root_right.val:
                return False
        left_right = root_left.right.val if root_left.right is not None else float(inf)
        right_left = root_right.left.val if root_right.left is not None else float(inf)
        left_left = root_left.left.val if root_left.left is not None else float(inf)
        right_right = root_right.right.val if root_right.right is not None else float(inf)
        if left_right != right_left or left_left != right_right:
            return False
        else:
            one_half = self.isSymmetric(root_left.right, root_right.left, depth=depth+1)
            if not one_half:
                return one_half
            two_half = self.isSymmetric(root_left.left, root_right.right, depth=depth+1)
            return two_half