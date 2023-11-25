# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.node_count = 0
        self.kth_smallest = 0
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root is None:
            return

        self.kthSmallest(root.left, k)
        self.node_count += 1
        if self.node_count == k:
            self.kth_smallest = root.val
            return self.kth_smallest
        self.kthSmallest(root.right, k)
        return self.kth_smallest