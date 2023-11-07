# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        from collections import deque
        self.level_values = []
        self.frontier = deque()
        self.stack = deque()

    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if root is None:
            return

        if not self.frontier:
            self.frontier.append(root)

        temp_vals = []
        while self.frontier:
            f_node = self.frontier.pop()
            temp_vals.append(f_node.val)
            if f_node.right:
                self.stack.append(f_node.right)
            if f_node.left:
                self.stack.append(f_node.left)
        print(temp_vals)
        if temp_vals:
            self.level_values.append(sum(temp_vals) / len(temp_vals))
        if self.stack:
            self.frontier = self.stack
            self.stack = deque()
            self.averageOfLevels(root)
        return self.level_values





