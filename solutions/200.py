class Solution:
    def __init__(self):
        self.islands = 0
        self.grid = []
        self.m = 0
        self.n = 0

    def numIslands(self, grid: List[List[str]]) -> int:
        self.m = len(grid)
        self.n = len(grid[0])
        self.grid = grid

        def find_island_dims(i, j):
            if int(self.grid[i][j]) != 1:
                return

            self.grid[i][j] = -1

            if j + 1 < self.n:
                find_island_dims(i, j + 1)
            if j - 1 >= 0:
                find_island_dims(i, j - 1)

            if i + 1 < self.m:
                find_island_dims(i + 1, j)
            if i - 1 >= 0:
                find_island_dims(i - 1, j)

            return

        for row in range(0, self.m):
            for col in range(0, self.n):
                if int(self.grid[row][col]) == 1:
                    self.islands += 1
                    find_island_dims(row, col)
        return self.islands

