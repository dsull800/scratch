class Solution:
    def __init__(self):
        self.board_graph = {}

    def snakesAndLadders(self, board: List[List[int]]) -> int:
        from collections import deque
        m = n = len(board)

        def get_x_y(value):
            ### get x,y from square_value
            x = n - math.ceil(value / n)
            y = (value - 1) % n if (n - (x + 1)) % 2 == 0 else n - 1 - ((value - 1) % n)
            return x, y

        frontier = deque()
        frontier.append([1, 0])
        visit = set()

        while frontier:
            value, moves = frontier.pop()
            for square in range(value + 1, min(value + 6, n ** 2) + 1):
                x, y = get_x_y(square)
                if board[x][y] != -1:
                    square = board[x][y]
                if square == n ** 2:
                    return moves + 1
                if square not in visit:
                    visit.add(square)
                    frontier.appendleft([square, moves + 1])

        return -1
