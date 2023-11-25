class Solution:
    def __init__(self):
        self.m = 0
        self.n = 0
        self.board = []
        self.visited = []

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.m = len(self.board)
        self.n = len(self.board[0])
        self.visited = [[False] * self.n for i in range(0, self.m)]
        self.board = board

        def zero_flipper(i, j, exterior=False):
            if not self.visited[i][j] and self.board[i][j] == 'O':
                self.visited[i][j] = True
                if not exterior:
                    self.board[i][j] = 'X'
                if i - 1 >= 0:
                    zero_flipper(i - 1, j, exterior)
                if i + 1 < self.m:
                    zero_flipper(i + 1, j, exterior)
                if j - 1 >= 0:
                    zero_flipper(i, j - 1, exterior)
                if j + 1 < self.n:
                    zero_flipper(i, j + 1, exterior)
            else:
                self.visited[i][j] = True

        for row in [0, self.m - 1]:
            for col in range(0, self.n):
                zero_flipper(row, col, True)

        for col in [0, self.n - 1]:
            for row in range(0, self.m):
                zero_flipper(row, col, True)

        for row in range(1, self.m - 1):
            for col in range(1, self.n - 1):
                zero_flipper(row, col)

