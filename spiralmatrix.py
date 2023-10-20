matrix = [[1,2,3],[4,5,6],[7,8,9]]


def spiralOrder(matrix):
    m = len(matrix)
    n = len(matrix[0])
    visited = 0
    i = 0
    j = 0
    res = []
    i_inc = 0
    j_inc = 1
    prev_inc = -1
    curr_inc = 1
    while visited < m * n - 1:
        if i < m and j < n and i >= 0 and j >= 0 and matrix[i][j] is not None:
            res.append(matrix[i][j])
            print(matrix[i][j])
            matrix[i][j] = None
            visited += 1
        else:
            if j_inc > 0:
                j = j - 1
            elif j_inc < 0:
                j = j + 1
            if i_inc > 0:
                i = i - 1
            elif i_inc < 0:
                i = i + 1

            if prev_inc == curr_inc:
                prev_inc, curr_inc = curr_inc, -curr_inc
            else:
                prev_inc, curr_inc = curr_inc, -prev_inc

            i_inc, j_inc = abs(j_inc), abs(i_inc)
        print(res)
        i += i_inc * curr_inc
        j += j_inc * curr_inc
        print(f'{i}, {j}')
        print(f'{prev_inc}, {curr_inc}')
        print(f'{i_inc}, {j_inc}')
        if res[-1] == 7:
            break

    return res

spiralOrder(matrix)