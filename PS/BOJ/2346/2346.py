#!/usr/bin/env python3

from collections import deque

def pop_balloons(balloons):
    q = deque([ [i+1, balloons[i]] for i in range(len(balloons)) ])
    orders = []
    while len(q) > 0:
        order, move = q.popleft()
        orders.append(order)
        rotate_cnt = move - 1 if move > 0 else move
        # Rotate order is opposite
        q.rotate(-rotate_cnt)
    return orders

if __name__ == '__main__':
    balloon_cnt = int(input())
    balloons = list(map(int, input().split()))
    orders = pop_balloons(balloons)
    print(*orders)
