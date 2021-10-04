#!/usr/bin/env python3

kbd_tbl = { 'q': [0, 0], 'w': [0, 1], 'e': [0, 2], 'r': [0, 3], 't': [0, 4],
        'y': [0, 5], 'u': [0, 6], 'i': [0, 7], 'o': [0, 8], 'p': [0, 9],
        'a': [1, 0], 's': [1, 1], 'd': [1, 2], 'f': [1, 3], 'g': [1, 4],
        'h': [1, 5], 'j': [1, 6], 'k': [1, 7], 'l': [1, 8], 'z': [2, 0],
        'x': [2, 1], 'c': [2, 2], 'v': [2, 3], 'b': [2, 4], 'n': [2, 5],
        'm': [2, 6] }

def get_elapsed(src, dst):
    elapsed = 1
    src_pos, dst_pos = kbd_tbl[src], kbd_tbl[dst]
    elapsed += max(src_pos[0], dst_pos[0]) - min(src_pos[0], dst_pos[0])
    elapsed += max(src_pos[1], dst_pos[1]) - min(src_pos[1], dst_pos[1])
    return elapsed

kr_consonants = "qwertasdfgzxcv"

if __name__ == '__main__':
    l, r = input().split()
    given_str = input()
    elapsed_time = 0
    for c in given_str:
        if c in kr_consonants:
            elapsed_time += get_elapsed(l, c)
            l = c
        else:
            elapsed_time += get_elapsed(r, c)
            r = c
    print(elapsed_time)
