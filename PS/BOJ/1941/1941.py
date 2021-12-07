#!/usr/bin/env python3

from collections import deque


idx_to_rc = lambda idx: (idx // 5, idx % 5)
rc_to_idx = lambda r, c: r * 5 + c

def are_neighbors(idx1, idx2):
    r1, c1 = idx_to_rc(idx1)
    r2, c2 = idx_to_rc(idx2)
    return abs(r1-r2) + abs(c1-c2) == 1


def is_valid_group(grp):
    visited = [grp[0]]
    que = deque([grp[0]])
    while len(que) > 0 and len(visited) < 7:
        cur = que.popleft()
        for next in grp:
            if next in visited:
                continue
            if are_neighbors(cur, next):
                visited.append(next)
                que.append(next)
    return len(visited) == 7


def get_groups(tbl, idx, grp = [], stat = [0, 0]):
    if len(grp) == 7:
        # Check if selected groups are all neighbors
        if is_valid_group(grp):
            yield [ i for i in grp ]
        return
    elif len(grp) == 0:
        grp = [idx]
        stat = [0, 0]
        r, c = idx_to_rc(idx)
        team = 0 if tbl[r][c] == 'S' else 1
        stat[team] += 1
        yield from get_groups(tbl, idx+1, grp, stat)
        return

    for next in range(idx, min(25, idx+6)):
        # Skip when Y team may exceed more than half
        r, c = idx_to_rc(next)
        team = 0 if tbl[r][c] == 'S' else 1
        if team == 1 and stat[1] == 3:
            continue

        stat[team] += 1
        grp.append(next)
        yield from get_groups(tbl, next+1, grp, stat)
        stat[team] -= 1
        grp.pop()


if __name__ == '__main__':
    tbl = []
    for _ in range(5):
        row = input()
        tbl.append(row)

    answers = []
    for idx in range(25-6):
        avail_grps = get_groups(tbl, idx)
        for g in avail_grps:
            answers.append(g)
    
    print(len(answers))
