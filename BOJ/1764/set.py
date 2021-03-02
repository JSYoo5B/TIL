#!/usr/bin/env python3

if __name__ == '__main__':
    cnt_n_heard, cnt_n_seen = map(int, input().split())
    n_heards, n_seens = set(), set()
    for i in range(cnt_n_heard):
        n_heard = input()
        n_heards.add(n_heard)
    for i in range(cnt_n_seen):
        n_seen = input()
        n_seens.add(n_seen)

    n_heard_seens = list(n_heards & n_seens)
    n_heard_seens.sort()
    print(len(n_heard_seens))
    for p in n_heard_seens:
        print(p)
