# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        from collections import deque
        self.levels = []
        self.frontier = deque()
        self.stack = deque()
        self.zig = False

    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root is None:
            return self.levels

        if not self.frontier:
            self.frontier.append(root)
            # self.levels.append([root.val])

        temp_arr = []
        while self.frontier:
            f_node = self.frontier.popleft()

            if f_node.left:
                self.stack.append(f_node.left)

            if f_node.right:
                self.stack.append(f_node.right)

            if self.zig:
                temp_arr = [f_node.val] + temp_arr
            else:
                temp_arr.append(f_node.val)

        if temp_arr:
            self.levels.append(temp_arr)

        if self.stack:
            self.frontier = self.stack
            self.stack = deque()
            self.zig = not self.zig
            self.zigzagLevelOrder(root)
        return self.levels
