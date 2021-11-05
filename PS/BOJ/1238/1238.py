#!/usr/bin/env python3

import heapq

INF = 10 ** 9
input = __import__('sys').stdin.readline
heappush = heapq.heappush
heappop = heapq.heappop


def get_dist_to_others(edges, src):
    nodes_cnt = len(edges)
    dists = [INF for _ in range(nodes_cnt)]
    heap = [ [0, src] ]
    while len(heap) > 0:
        [dist, node] = heappop(heap)
        dists[node] = min(dists[node], dist)
        for n, d in edges[node]:
            if dist + d < dists[n]:
                dists[n] = dist + d
                heappush(heap, [dists[n], n])
    return dists


if __name__ == '__main__':
    nodes_cnt, edges_cnt, tgt_id = map(int, input().split())
    tgt_id -= 1 # convert into zero offset
    edges = [ [ ] for _ in range(nodes_cnt) ]
    for _ in range(edges_cnt):
        src, dst, dist = map(int, input().split())
        edges[src-1].append([dst-1, dist])
    
    single_dists = []
    for n in range(nodes_cnt):
        dist = get_dist_to_others(edges, n)
        single_dists.append(dist)
    
    return_dists = []
    for n in range(nodes_cnt):
        dist = single_dists[n][tgt_id] + single_dists[tgt_id][n]
        return_dists.append(dist)
    answer = max(return_dists)
    print(answer)
