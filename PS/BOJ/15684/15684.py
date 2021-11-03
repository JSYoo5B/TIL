#!/usr/bin/env python3


from itertools import combinations

input = __import__('sys').stdin.readline

def check_modified_ladder(ladder, extra):
    player_cnt, height = len(ladder[0]), len(ladder)

    for p in range(player_cnt):
        start = p
        for h in range(height):
            p += ladder[h][p] + extra[h][p]
        if p != start:
            return False
    return True


def create_extra(conn_info, player_cnt, height):
    extra = [ [ 0 for _ in range(player_cnt) ] for _ in range(height) ]
    for [h, pos] in conn_info:
        extra[h][pos] = 1
        extra[h][pos+1] = -1
    return extra


if __name__ == '__main__':
    player_cnt, ladder_cnt, height = map(int, input().split())
    ladder = [ [ 0 for _ in range(player_cnt) ] for _ in range(height) ]
    for _ in range(ladder_cnt):
        h, pos = map(int, input().split())
        ladder[h-1][pos-1] = 1
        ladder[h-1][pos] = -1

    # Find available connections
    avail_conn = []
    for h in range(height):
        for p in range(player_cnt - 1):
            if ladder[h][p] == 0 and ladder[h][p+1] == 0:
                avail_conn.append([h, p])

    extra_req = -1
    blank = create_extra([], player_cnt, height)
    if check_modified_ladder(ladder, blank) == True:
        extra_req = 0
    for ext_cnt in range(1, 4):
        if extra_req != -1:
            break
        for select in combinations(avail_conn, ext_cnt):
            extra = create_extra(select, player_cnt, height)
            if check_modified_ladder(ladder, extra) == True:
                extra_req = ext_cnt
                break
    print(extra_req)
