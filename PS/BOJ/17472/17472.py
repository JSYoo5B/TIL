#!/usr/bin/env python3

from collections import deque

UNKNOWN, BLANK = -1, 0

def enum_island(world_map, start_pos, id):
    row_cnt = len(world_map)
    col_cnt = len(world_map[0])

    que = deque([start_pos])
    world_map[start_pos[0]][start_pos[1]] = id
    while len(que) > 0:
        [r, c] = que.popleft()
        neighbors = [[r-1, c], [r+1, c], [r, c-1], [r, c+1]]
        for [n_r, n_c] in neighbors:
            if 0 > n_r or n_r >= row_cnt \
                    or 0 > n_c or n_c >= col_cnt:
                continue
            if world_map[n_r][n_c] == UNKNOWN:
                world_map[n_r][n_c] = id
                que.append([n_r, n_c])
    return


def get_edges(world_map, islands_cnt):
    edges = [ [ [0, [0, 0], [0, 0]] for _ in range(islands_cnt + 1) ] \
            for _ in range(islands_cnt + 1) ]

    # find bridges in horizontal
    for r in range(row_cnt):
        isle_start, isle_end = UNKNOWN, UNKNOWN
        dist = 0
        for c in range(col_cnt):
            if isle_start == UNKNOWN and world_map[r][c] != BLANK:
                # Start bridge
                isle_start = world_map[r][c]
                dist = 0
            elif isle_start != UNKNOWN and world_map[r][c] == isle_start:
                # Still in island, or connecting itself. move starting pos
                dist = 0
            elif isle_start != UNKNOWN and world_map[r][c] == BLANK:
                # Continue bridge
                dist += 1
            elif isle_start != UNKNOWN and world_map[r][c] != BLANK:
                # Connected to somewhere else
                isle_end = world_map[r][c]
                if dist > 1:
                    # Only bridges with longer than 1 will be considered
                    v1, v2 = min(isle_start, isle_end), max(isle_start, isle_end)
                    prev_edge = edges[v1][v2]
                    if prev_edge[0] == 0 or prev_edge[0] > dist:
                        # when the edge isn't set or it was longer, replace it
                        edges[v1][v2] = [dist, v1, v2] 
                # flush current bridge, treat as starting bridge
                isle_start, isle_end = world_map[r][c], UNKNOWN
                dist = 0
    # find bridges in vertical
    for c in range(col_cnt):
        isle_start, isle_end = UNKNOWN, UNKNOWN
        dist = 0
        for r in range(row_cnt):
            if isle_start == UNKNOWN and world_map[r][c] != BLANK:
                # Start bridge
                isle_start = world_map[r][c]
                dist = 0
            elif isle_start != UNKNOWN and world_map[r][c] == isle_start:
                # Still in island, or connecting itself. move starting pos
                dist = 0
            elif isle_start != UNKNOWN and world_map[r][c] == BLANK:
                # Continue bridge
                dist += 1
            elif isle_start != UNKNOWN and world_map[r][c] != BLANK:
                # Connected to somewhere else
                isle_end = world_map[r][c]
                if dist > 1:
                    # Only bridges with longer than 1 will be considered
                    v1, v2 = min(isle_start, isle_end), max(isle_start, isle_end)
                    prev_edge = edges[v1][v2]
                    if prev_edge[0] == 0 or prev_edge[0] > dist:
                        # when the edge isn't set or it was longer, replace it
                        edges[v1][v2] = [dist, v1, v2]
                # flush current bridge, treat as starting bridge
                isle_start, isle_end = world_map[r][c], UNKNOWN
                dist = 0
    # get only active edges
    actives = []
    for v1 in range(islands_cnt):
        for v2 in range(v1+1, islands_cnt):
            e = edges[v1+1][v2+1]
            if e[0] > 0:
                actives.append(e)
    return actives


def min_spanning_tree(edges, islands_cnt):
    edges.sort()
    tree = []
    parent = [ i for i in range(islands_cnt + 1) ]
    for [dist, isle_s, isle_d] in edges:
        if parent[isle_s] == parent[isle_d]:
            continue
        isle_d = parent[isle_d]
        parent[isle_d] = parent[isle_s]
        for i in range(1, islands_cnt):
            if parent[i] == i:
                continue
            parent[i] = parent[parent[i]]
        tree.append(dist)
        if len(tree) == islands_cnt - 1:
            break
    if len(tree) < islands_cnt - 1:
        tree = []
    return tree


if __name__ == '__main__':
    row_cnt, col_cnt = map(int, input().split())
    world_map = []
    for _ in range(row_cnt):
        row = list(map(int, input().split()))
        row = [ -1 * c for c in row ]
        world_map.append(row)

    # enumerate islands
    isle_id = 1
    for r in range(row_cnt):
        for c in range(col_cnt):
            if world_map[r][c] != -1:
                continue
            enum_island(world_map, [r, c], isle_id)
            isle_id += 1
    islands_cnt = isle_id - 1

    edges = get_edges(world_map, islands_cnt)
    bridges = min_spanning_tree(edges, islands_cnt)
    answer = sum(bridges)
    if answer == 0:
        answer = -1
    print(answer)

