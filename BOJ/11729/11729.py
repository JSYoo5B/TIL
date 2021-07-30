#!/usr/bin/env python3

def hanoi_tower(level, src, dst, tmp):
    if level == 0:
        return
    # Move upper disks to temporal pole
    hanoi_tower(level-1, src, tmp, dst)
    # Move actual disk
    print(src, dst)
    # Move upper disks from temporal to destination pole
    hanoi_tower(level-1, tmp, dst, src)

if __name__ == '__main__':
    disks = int(input())

    # Known hanoi tower steps formula
    total_count = 2 ** disks - 1
    print(total_count)

    hanoi_tower(disks, 1, 3, 2)
