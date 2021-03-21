#!/usr/bin/env python3

def dfs(node, graph, visited):
    visited.append(node)
    x, y = node[0], node[1]
    graph[x][y] = 0
    dirs = [ [x, y] for i in range(4) ]
    dirs[0][0] -= 1  # left
    dirs[1][0] += 1  # right
    dirs[2][1] -= 1  # up
    dirs[3][1] += 1  # down
    movables = [ d for d in dirs \
            if 0 <= d[0] and d[0] < len(graph) \
                and 0 <= d[1] and d[1] < len(graph) ]
    for m in movables:
        x, y = m[0], m[1]
        if graph[x][y] == 1:
            dfs(m, graph, visited)


if __name__ == '__main__':
    N = int(input())
    town_map = [ ]
    for i in range(N):
        map_row = input()
        numeric_map = [ int(i) for i in map_row ]
        town_map.append(numeric_map)

    groups = []
    for y in range(N):
        for x in range(N):
            if town_map[x][y] == 1:
                neighbors = []
                dfs([x, y], town_map, neighbors)
                groups.append(neighbors)

    groups.sort(key = lambda x: (len(x)))
    print(len(groups))
    for n in groups:
        print(len(n))
