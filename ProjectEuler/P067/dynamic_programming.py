#!/usr/bin/env python3
"""Dynamic programming solution
1. loop from top layer to bottom layer
2. for edge numbers(leftmost and rightmost), accumulate upper layer's edge number
3. for non-edge numbers, compare greatest sum of upper left or right number path
4. when the loop is done, find maximum value in the last(bottom) layer
"""

if __name__ == '__main__':
    with open('p067_triangle.txt') as file:
        triangle_txt = file.read()
        DATA = []
        for line in triangle_txt.strip().splitlines():
            DATA.append([int(i) for i in line.split()])

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
