#!/usr/bin/env python3

if __name__ == '__main__':
    waiting_cnt = int(input())
    pendings = list(map(int, input().split()))

    pendings.sort()
    waitings = [ sum(pendings[:i+1]) for i in range(len(pendings)) ]
    answer = sum(waitings)
    print(answer)
