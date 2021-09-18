#!/usr/bin/env python3

if __name__ == '__main__':
    scores = []
    scores.append(int(input()))
    scores.append(int(input()))
    scores.append(int(input()))
    scores.append(int(input()))
    scores.sort()
    scores.pop(0)
    E = int(input())
    F = int(input())
    scores.append(E if E > F else F)
    answer = sum(scores)
    print(answer)
