#!/usr/bin/env python3

import sys
from collections import deque

input = sys.stdin.readline

def get_hackable_pcs(trust_table, pc_id, pc_cnt):
    hacked = [ 0 for _ in range(pc_cnt + 1) ]
    hacked[pc_id] = 1
    pc_cnt = 1
    que = deque([pc_id])
    while len(que) > 0:
        current = que.popleft()
        for pc in trust_table[current]:
            if hacked[pc] == 0:
                hacked[pc] = 1
                pc_cnt += 1
                que.append(pc)
    return pc_cnt

if __name__ == '__main__':
    node_cnt, edge_cnt = map(int, input().split())
    trust_table = [ [] for _ in range(node_cnt + 1) ]
    for _ in range(edge_cnt):
        pc, trusting = map(int, input().split())
        trust_table[trusting].append(pc)
    
    hackables = [ get_hackable_pcs(trust_table, i+1, node_cnt) for i in range(node_cnt) ]
    max_hackable_cnt = max(hackables)
    candidates = []
    for i in range(node_cnt):
        if hackables[i] == max_hackable_cnt:
            candidates.append(i+1)
    print(*candidates)
