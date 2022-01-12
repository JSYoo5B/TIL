#!/usr/bin/env python3

from sys import setrecursionlimit
setrecursionlimit(10**9)

def mul_mat(mat1, mat2):
    row_size, col_size = len(mat1), len(mat2[0])
    mul_size = len(mat1[0])
    res_mat = [ [ 0 for _ in range(col_size) ] for _ in range(row_size) ]

    for r in range(row_size):
        for c in range(col_size):
            for i in range(mul_size):
                res_mat[r][c] += mat1[r][i] * mat2[i][c]
            res_mat[r][c] %= 1000000
    return res_mat


def get_mat_power(mat, pow, memo = {}):
    if pow <= 1:
        memo[pow] = mat

    if memo.get(pow, None) != None:
        return memo[pow]

    mat_half = get_mat_power(mat, pow // 2, memo)
    memo[pow // 2 * 2] = mul_mat(mat_half, mat_half)
    if pow % 2 == 1:
        memo[pow] = mul_mat(memo[pow-1], mat)
    return memo[pow]


if __name__ == '__main__':
    index = int(input())
    mat = [[1, 1], [1, 0]]

    result = get_mat_power(mat, index)
    answer = result[0][-1]
    if index == 0:
        answer = 0
    print(answer)

