# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return

        def preorder_traverse(root):
            if root is None:
                return

            left_list = preorder_traverse(root.left)
            right_list = preorder_traverse(root.right)
            root.left = None
            if left_list is not None:
                root.right = left_list
                while left_list.right is not None:
                    left_list = left_list.right
                left_list.right = right_list
            else:
                root.right = right_list
            return root

        preorder_traverse(root)
