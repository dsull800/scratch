class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        def find_next(row, col, word):
            if word == '' or word == board[row][col]:
                return True

            if board[row][col] == '#':
                return

            tmp = board[row][col]
            if tmp == word[0]:
                board[row][col] = '#'
                if row + 1 < m:
                    out = find_next(row + 1, col, word[1:])
                    if out:
                        return out
                if row - 1 >= 0:
                    out = find_next(row - 1, col, word[1:])
                    if out:
                        return out
                if col + 1 < n:
                    out = find_next(row, col + 1, word[1:])
                    if out:
                        return out
                if col - 1 >= 0:
                    out = find_next(row, col - 1, word[1:])
                    if out:
                        return out

                board[row][col] = tmp

            else:
                return

        for row in range(0, m):
            for col in range(0, n):
                out = find_next(row, col, word)
                if out:
                    return out
        return False