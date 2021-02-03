#!/usr/bin/env python3
"""Dynamic programming solution
1. loop from top layer to bottom layer
2. for edge numbers(leftmost and rightmost), accumulate upper layer's edge number
3. for non-edge numbers, compare greatest sum of upper left or right number path
4. when the loop is done, find maximum value in the last(bottom) layer
"""

DATA = [
    [75],
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20,  4, 82, 47, 65],
    [19,  1, 23, 75,  3, 34],
    [88,  2, 77, 73,  7, 63, 67],
    [99, 65,  4, 28,  6, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23]
]

if __name__ == '__main__':
    accum = DATA

    for layer in range(1, len(accum)):
        for idx in range(0, len(accum[layer])):
            if idx == 0:
                accum[layer][0] += accum[layer - 1][0]
            elif idx == len(accum[layer])-1:
                accum[layer][-1] += accum[layer - 1][-1]
            else:
                accum[layer][idx] += max(accum[layer - 1][idx - 1:idx + 1])

    answer = max(accum[len(accum)-1])
    print(answer)
