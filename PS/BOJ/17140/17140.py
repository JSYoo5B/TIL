#!/usr/bin/env python3

def transpose_matrix(matrix):
    return [list(i) for i in zip(*matrix)]

def do_R_operation(matrix):
    new_matrix = []
    for row in matrix:
        counters = [ 0 for _ in range(101) ]
        for elem in row:
            if elem > 0:
                counters[elem] += 1
        count_pairs = []
        for i in range(1, 101):
            if counters[i] > 0:
                count_pairs.append([i, counters[i]])
        count_pairs.sort(key = lambda x: (x[1], x[0]))
        new_row = []
        for c in count_pairs:
            new_row += c
        new_matrix.append(new_row)
    max_row_cnt = max([ len(row) for row in new_matrix ])
    if max_row_cnt > 100:
        max_row_cnt = 100
    next_matrix = []
    for row in new_matrix:
        diff = max_row_cnt - len(row)
        if diff <= 0:
            next_matrix.append(row[:max_row_cnt])
        else:
            next_matrix.append(row + [0 for _ in range(diff)])
    return next_matrix

if __name__ == '__main__':
    row_pos, col_pos, desired_val = map(int, input().split())
    row_pos -= 1
    col_pos -= 1
    matrix = []
    for _ in range(3):
        row = list(map(int, input().split()))
        matrix.append(row)

    operation_cnt = 0
    transpose = False
    while operation_cnt <= 100:
        row_max = len(matrix)
        col_max = len(matrix[0])
        if row_pos < row_max and col_pos < col_max \
                and matrix[row_pos][col_pos] == desired_val:
                    break
        if row_max < col_max:
            matrix = transpose_matrix(matrix)
        matrix = do_R_operation(matrix)
        if row_max < col_max:
            matrix = transpose_matrix(matrix)
        operation_cnt += 1

    if operation_cnt > 100:
        operation_cnt = -1
    print(operation_cnt)
