class Solution:
    def __init__(self):
        self.board_graph = {}

    def snakesAndLadders(self, board: List[List[int]]) -> int:
        m = n = len(board)

        def get_x_y(value):
            ### get x,y from square_value
            x = n - math.ceil(value / n)
            y = (value - 1) % n if (n - (x + 1)) % 2 == 0 else n - 1 - ((value - 1) % n)
            return x, y

        def get_next_value(value):
            x, y = get_x_y(value)
            return board[x][y] if board[x][y] != -1 else value

        def dfs(value, current_stack, laddered=False):
            x, y = get_x_y(value)
            # not laddered  or board[x][y] == -1
            if (board[x][y] == -1) and self.board_graph.get(value, None) is not None:
                return self.board_graph[value] + int(not laddered)

            if value == n ** 2:
                return int(not laddered)

            elif board[x][y] == -1 or laddered:
                min_out = 999999
                sorted_values = sorted(list(range(value + 1, min(value + 6, n ** 2) + 1)), key=get_next_value)
                for square in sorted_values:  # range(value + 1, min(value + 6, n ** 2) + 1):
                    if square not in current_stack:
                        new_stack = list(range(value + 1, min(value + 6, n ** 2) + 1)) + current_stack
                        out = dfs(square, new_stack, False)
                        min_out = min(out, min_out)
                if not laddered:
                    self.board_graph[value] = min(min_out, self.board_graph.get(value, 999999))

                return (min_out + int(not laddered)) if laddered else (
                            self.board_graph.get(value, min_out) + int(not laddered))

            elif board[x][y] != -1 and not laddered:
                if board[x][y] not in current_stack:
                    new_stack = [i for i in current_stack]  # + [board[x][y]]
                    out = dfs(board[x][y], new_stack, laddered=True)
                    self.board_graph[value] = min(out, self.board_graph.get(value, 999999))
                    return self.board_graph[value] + int(not laddered)
                return 999999

            else:
                raise Exception('What the hell')

        # for i in sorted(list(range(n**2, 0, -1)), key=get_next_value):
        dfs(1, [1], False)
        my_keys = list(self.board_graph.keys())
        my_keys.sort(reverse=True)
        print({i: self.board_graph[i] for i in my_keys})
        return self.board_graph[1] if self.board_graph[1] < 999999 else -1