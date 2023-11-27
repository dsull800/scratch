"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        #root_node = Node(val=1, isLeaf=0)#, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None)
        print(grid)
        m = n = len(grid)

        reduced_grid = reduce(lambda x,y: x+y, grid)
        if n == 1 or all(ele == reduced_grid[0] for ele in reduced_grid):
            return Node(val=grid[0][0], isLeaf=1)#, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None)

        root_node = Node(val=1, isLeaf=0)
        n_over_2 = int(n/2)
        root_node.topLeft = self.construct([row[0:n_over_2] for row in grid[0:n_over_2]])
        root_node.topRight = self.construct([row[n_over_2:] for row in grid[0:n_over_2]])
        root_node.bottomLeft = self.construct([row[0:n_over_2] for row in grid[n_over_2:]])
        root_node.bottomRight = self.construct([row[n_over_2:] for row in grid[n_over_2:]])


        return root_node