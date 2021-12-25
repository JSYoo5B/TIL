#!/usr/bin/env python3

from sys import setrecursionlimit
setrecursionlimit(10**6)

prefix, infix, postfix = [], [], []
infix_idx = []

def prefix_fill(inf_l, inf_r, post_l, post_r):
    if post_l > post_r or inf_l > inf_r:
        return

    parent = postfix[post_r]
    p_idx = infix_idx[parent]

    # last postfix is parent. in prefix, it's heading
    prefix.append(parent)

    # traverse left infix
    l_len = p_idx - inf_l - 1
    prefix_fill(inf_l, inf_l+l_len, post_l, post_l+l_len)

    # traverse right infix
    r_len = inf_r - p_idx
    prefix_fill(inf_r-r_len+1, inf_r, post_r-r_len, post_r-1)


if __name__ == '__main__':
    nodes_cnt = int(input())
    infix = list(map(int, input().split()))
    postfix = list(map(int, input().split()))

    infix_idx = [ 0 for _ in range(nodes_cnt+1) ]
    for i in range(nodes_cnt):
        infix_idx[infix[i]] = i
    prefix_fill(0, nodes_cnt-1, 0, nodes_cnt-1)
    print(*prefix)

