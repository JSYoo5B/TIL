#!/usr/bin/env python3

from sys import stdin
input = stdin.readline

if __name__ == '__main__':
    tbl_size, slide_len = map(int, input().split())
    tbl = []
    for _ in range(tbl_size):
        row = list(map(int, input().split()))
        tbl.append(row)

    for c in range(tbl_size):
        column = [ tbl[r][c] for r in range(tbl_size) ]
        tbl.append(column)

    answer = 0
    for row in tbl:
        comp_line = []
        for e in row:
            if len(comp_line) == 0 or comp_line[-1][0] != e:
                comp_line.append([e, 1])
            elif comp_line[-1][0] == e:
                comp_line[-1][1] += 1

        valid = True
        for cur in range(len(comp_line)-1):
            next = cur + 1
            if abs(comp_line[cur][0] - comp_line[next][0]) > 1:
                valid = False
                break
            if comp_line[cur][0] > comp_line[next][0]:
                comp_line[next][1] -= slide_len
            elif comp_line[cur][0] < comp_line[next][0]:
                comp_line[cur][1] -= slide_len

            if comp_line[cur][1] < 0 or comp_line[next][1] < 0:
                valid = False
                break
        if valid:
            answer += 1
    print(answer)
