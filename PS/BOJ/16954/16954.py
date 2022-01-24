#!/usr/bin/env python3

from collections import deque

def traversal(tbl):
    visited = [ [ False for _ in range(8) ] for _ in range(16) ]
    que = deque([ [0, 0, 0] ])
    visited[0][0] = True
    answer = 0
    while len(que) > 0:
        r, c, step = que.popleft()
        if step == 8:
            answer = 1
            break
        for n_r, n_c in [ [r, c-1], [r, c], [r, c+1], \
                [r+1, c-1], [r+1, c], [r+1, c+1], \
                [r-1, c-1], [r-1, c], [r-1, c+1]]:
            if n_r in [-1, 8] or n_c in [-1, 8]:
                continue
            if tbl[n_r+step][n_c] == '.' and tbl[n_r+step+1][n_c] == '.' \
                    and visited[n_r+step+1][n_c] == False:
                visited[n_r+step+1][n_c] = True
                que.append([n_r, n_c, step+1])
    return answer


if __name__ == '__main__':
    tbl = []
    for _ in range(8):
        line = input()
        row = [ c for c in line ]
        tbl.append(row)
    tbl.reverse()
    for _ in range(8):
        tbl.append([ '.' for _ in range(8) ])

    answer = traversal(tbl)
    print(answer)
