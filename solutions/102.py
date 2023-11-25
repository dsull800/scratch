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

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return self.levels

        if not self.levels:
            self.levels.append([root.val])
            if root.left:
                self.frontier.append(root.left)
            if root.right:
                self.frontier.append(root.right)

        temp_arr = []
        while self.frontier:
            root = self.frontier.popleft()
            temp_arr.append(root.val)
            if root.left:
                self.stack.append(root.left)
            if root.right:
                self.stack.append(root.right)

        if temp_arr:
            self.levels.append(temp_arr)

        if self.stack:
            self.frontier = self.stack
            self.stack = deque()
            self.levelOrder(root)

        return self.levels
