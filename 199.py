# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        from collections import deque
        self.output = []
        self.stack = deque()
        self.frontier = deque()

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return
        if not self.frontier:
            self.output.append(root.val)
            self.frontier.append(root)

        while self.frontier:
            f_node = self.frontier.popleft()
            if f_node.left is not None:
                self.stack.append(f_node.left)
            if f_node.right is not None:
                self.stack.append(f_node.right)
        if self.stack:
            self.output.append(self.stack[-1].val)
        self.frontier = self.stack
        if self.frontier:
            self.stack = deque()
            self.rightSideView(self.frontier[-1])
        return self.output
