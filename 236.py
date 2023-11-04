# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return TreeNode(False)

        current = root == q or root == p

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if (current and left.val) or (current and right.val):
            return root

        elif current:
            return TreeNode(True)

        if (right.val or left.val or not isinstance(left.val, bool) or not isinstance(right.val, bool)):
            if not isinstance(left.val, bool):
                return left
            elif not isinstance(right.val, bool):
                return right
            else:
                if right.val and left.val:
                    return root
                else:
                    return TreeNode(True)
        else:
            return TreeNode(False)