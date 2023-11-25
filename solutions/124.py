# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return curr_path_sum

        ## subtree max paths, left leaf -> interior node -> right leaf,
        ## root -> left leaf, root -> right leaf
        def max_path_finder(root, interior_max = 0, root_left= 0, root_right = 0):
            if root is None:
                return -10000, 0, 0

            left_interior_max, left_left_max, left_right_max = max_path_finder(root.left)
            right_interior_max, right_left_max, right_right_max = max_path_finder(root.right)

            right_root_left = max(right_left_max, right_right_max,0) + root.val + max(left_left_max, left_right_max,0)
            return max(left_interior_max, right_interior_max, right_root_left), root.val + max(left_left_max, left_right_max, 0), root.val + max(right_left_max, right_right_max, 0)

        return max(max_path_finder(root))
