#!/usr/bin/env python3

from collections import deque
from collections import defaultdict

def puzzle_to_nonary(state):
    nonary = 0
    for i in state:
        nonary *= 9
        nonary += i
    return nonary


def nonary_to_puzzle(nonary):
    puzzle = [ ]
    for _ in range(9):
        radix = nonary % 9
        puzzle.append(radix)
        nonary //= 9
    puzzle.reverse()
    return puzzle


END_STATE = [1, 2, 3, 4, 5, 6, 7, 8, 0]
END_NONARY = puzzle_to_nonary(END_STATE)

def try_to_solve(state):
    start_nonary = puzzle_to_nonary(state)
    if start_nonary == END_NONARY:
        return 0
    visited = defaultdict(int)
    visited[start_nonary] = 1
    que = deque([[start_nonary, 0]])
    while len(que) > 0:
        [nonary, trial] = que.popleft()
        if nonary == END_NONARY:
            return trial
        state = nonary_to_puzzle(nonary)
        b_pos = state.index(0)
        neighbors = [ b_pos-1, b_pos+1, b_pos-3, b_pos+3 ]
        for n in neighbors:
            if 0 > n or n >= 9:
                continue
            if b_pos % 3 == 2 and n - b_pos == 1:
                continue
            elif b_pos % 3 == 0 and b_pos - n == 1:
                continue
            state[n], state[b_pos] = state[b_pos], state[n]
            next = puzzle_to_nonary(state)
            if visited[next] == 0:
                visited[next] = 1
                que.append([next, trial+1])
            state[n], state[b_pos] = state[b_pos], state[n]
    return -1


if __name__ == '__main__':
    state = []
    for _ in range(3):
        row = list(map(int, input().split()))
        state += row

    answer = try_to_solve(state)
    print(answer)
