class Solution:
    def totalNQueens(self, n: int) -> int:
        rows = list(range(0, n))
        columns = list(range(0, n))
        res = []
        diag_modulo = set([(0, j) for j in range(0, n)] + [(i, 0) for i in range(0, n)])

        def find_placement(row, columns, combo, board_modulo, diag_modulo):
            if len(combo) == n:
                res.append(combo[:])
            if not rows or not columns:
                return

            row += 1
            for col_ind, column in enumerate(columns):
                mrc = min(row, column)
                if row + column in board_modulo and (row - mrc, column - mrc) in diag_modulo:
                    board_modulo.remove(row + column)
                    diag_modulo.remove((row - mrc, column - mrc))
                    combo.append((row, column))
                    find_placement(row, columns[:col_ind] + columns[col_ind + 1:], combo, board_modulo, diag_modulo)
                    combo.pop()
                    board_modulo.add(row + column)
                    diag_modulo.add((row - mrc, column - mrc))

        find_placement(-1, columns, [], set(list(range(0, (n - 1) ** 2 + 1))), diag_modulo)

        return len(res)