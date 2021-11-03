#!/usr/bin/env python3

import sys

sys.setrecursionlimit(1000000)

input = sys.stdin.readline

def do_acm_craft(build_info, depends, target, memo):
    if memo[target] > -1:
        return memo[target]
    deps_info = depends[target]
    if len(deps_info) == 0:
        memo[target] = build_info[target]
        return memo[target]

    build_deps = []
    for d in deps_info:
        b_d = do_acm_craft(build_info, depends, d, memo)
        build_deps.append(b_d)

    memo[target] = build_info[target] + max(build_deps)
    return memo[target]


if __name__ == '__main__':
    round_cnt = int(input())
    for _ in range(round_cnt):
        build_cnt, deps_cnt = map(int, input().split())
        build_info = list(map(int, input().split()))
        deps = [ [] for _ in range(build_cnt) ]
        for _ in range(deps_cnt):
            prec, eff = map(int, input().split())
            deps[eff-1].append(prec-1)
        target = int(input()) - 1
        
        memo = [-1 for _ in range(build_cnt) ]
        answer = do_acm_craft(build_info, deps, target, memo)
        print(answer)
