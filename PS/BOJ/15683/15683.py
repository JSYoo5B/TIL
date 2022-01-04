#!/usr/bin/env python3

from copy import deepcopy

# directions
EMPTY, UP, LEFT, DOWN, RIGHT = 0, 1, 2, 3, 4

# camera types
SPACE, SINGLE, BIDIR, ORTHO, TRIANGLE, ALL, WALL = 0, 1, 2, 3, 4, 5, 6

def get_cameras(tbl):
    row_sz, col_sz = len(tbl), len(tbl[0])
    cameras = [ ]
    for r in range(row_sz):
        for c in range(col_sz):
            type = tbl[r][c]
            if 0 < type < 6:
                cameras.append([type, r, c, EMPTY])
    return cameras


def get_dead_zone_cnt(tbl):
    answer = 0
    for row in tbl:
        answer += row.count(0)
    return answer


def place_cam(tbl, cam_pos, cam_type, dir):
    [c_r, c_c] = cam_pos
    row_sz, col_sz = len(tbl), len(tbl[0])
    surveil_cnt = 0
    # UP
    if cam_type == ALL \
            or (cam_type == TRIANGLE and dir != DOWN) \
            or (cam_type == ORTHO and dir in [UP, LEFT]) \
            or (cam_type == BIDIR and dir in [UP, DOWN]) \
            or (cam_type == SINGLE and dir == UP):
        for r in range(c_r-1, -1, -1):
            if tbl[r][c_c] == WALL:
                break
            elif tbl[r][c_c] != SPACE:
                continue
            tbl[r][c_c] = -1
            surveil_cnt += 1

    # LEFT
    if cam_type == ALL \
            or (cam_type == TRIANGLE and dir != RIGHT) \
            or (cam_type == ORTHO and dir in [LEFT, DOWN]) \
            or (cam_type == BIDIR and dir in [LEFT, RIGHT]) \
            or (cam_type == SINGLE and dir == LEFT):
        for c in range(c_c-1, -1, -1):
            if tbl[c_r][c] == WALL:
                break
            elif tbl[c_r][c] != SPACE:
                continue
            tbl[c_r][c] = -1
            surveil_cnt += 1

    # DOWN
    if cam_type == ALL \
            or (cam_type == TRIANGLE and dir != UP) \
            or (cam_type == ORTHO and dir in [DOWN, RIGHT]) \
            or (cam_type == BIDIR and dir in [UP, DOWN]) \
            or (cam_type == SINGLE and dir == DOWN):
        for r in range(c_r+1, row_sz):
            if tbl[r][c_c] == WALL:
                break
            elif tbl[r][c_c] != SPACE:
                continue
            tbl[r][c_c] = -1
            surveil_cnt += 1

    # RIGHT
    if cam_type == ALL \
            or (cam_type == TRIANGLE and dir != LEFT) \
            or (cam_type == ORTHO and dir in [RIGHT, UP]) \
            or (cam_type == BIDIR and dir in [LEFT, RIGHT]) \
            or (cam_type == SINGLE and dir == RIGHT):
        for c in range(c_c+1, col_sz):
            if tbl[c_r][c] == WALL:
                break
            elif tbl[c_r][c] != SPACE:
                continue
            tbl[c_r][c] = -1
            surveil_cnt += 1

    return surveil_cnt


def place_cameras(tbl, cameras, dead_cnt = -1, cur = -1):
    if dead_cnt == -1:
        dead_cnt = get_dead_zone_cnt(tbl)
        cur = len(cameras)-1
    if dead_cnt == 0 or cur == -1:
        yield dead_cnt
        return

    [type, r, c, cur_dir] = cameras[cur]
    avail_dirs = [UP, LEFT, DOWN, RIGHT]
    if type == BIDIR:
        avail_dirs = [UP, LEFT]
    for dir in avail_dirs:
        cameras[cur][3] = dir
        new_tbl = deepcopy(tbl)
        diff = place_cam(new_tbl, [r, c], type, dir)
        yield from place_cameras(new_tbl, cameras, dead_cnt-diff, cur-1)
    cameras[cur][3] = EMPTY


if __name__ == '__main__':
    row_sz, col_sz = map(int, input().split())
    tbl = []
    for _ in range(row_sz):
        row = list(map(int, input().split()))
        tbl.append(row)
    
    cameras = get_cameras(tbl)
    while len(cameras) > 0 and cameras[-1][0] == ALL:
        [type, r, c, dir] = cameras.pop()
        place_cam(tbl, [r, c], 5, dir)

    answers = list(place_cameras(tbl, cameras))
    print(min(answers))
