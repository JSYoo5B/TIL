#!/usr/bin/env python3

if __name__ == '__main__':
    height = int(input())
    triangle = []
    for i in range(height):
        layer = list(map(int, input().split()))
        triangle.append(layer)

    for level in range(1, height):
        for i in range(0, len(triangle[level])):
            # Edge case must choose upper layer's edge numbers
            if i == 0:
                triangle[level][0] += triangle[level-1][0]
                continue
            elif i == len(triangle[level])-1:
                triangle[level][i] += triangle[level-1][i-1]
                continue
            # In general, choose max number of upper layer's near numbers
            triangle[level][i] \
                    += max(triangle[level-1][i-1], triangle[level-1][i])
    
    answer = max(triangle[height-1])
    print(answer)
