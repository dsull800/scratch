"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        from collections import deque
        queue = deque()
        prev_depth = 0
        queue.appendleft((root, prev_depth))
        prev_node = None
        while len(queue) > 0:
            new_node, new_depth = queue.pop()
            if new_node is None:
                continue
            if new_depth == prev_depth:
                new_node.next = prev_node
            else:
                new_node.next = None
            queue.appendleft((new_node.right, new_depth + 1))
            queue.appendleft((new_node.left, new_depth + 1))
            prev_depth = new_depth
            prev_node = new_node
        return root