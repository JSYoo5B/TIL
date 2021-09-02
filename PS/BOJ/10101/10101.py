#!/usr/bin/env python3

if __name__ == '__main__':
    angles = []
    for _ in range(3):
        angle = int(input())
        angles.append(angle)
    angles.sort()

    if sum(angles) != 180:
        print("Error")
    elif angles[0] == 60:
        print("Equilateral")
    elif angles[0] == angles[1] or angles[1] == angles[2]:
        print("Isosceles")
    else:
        print("Scalene")

