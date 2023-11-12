"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return
        clone_node = Node(node.val)
        node.clone_node = clone_node
        clone_node.neighbors = [clone_neighbor.clone_node if hasattr(clone_neighbor, 'clone_node') else self.cloneGraph(clone_neighbor) for clone_neighbor in node.neighbors]

        return clone_node