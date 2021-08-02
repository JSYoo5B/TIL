#!/usr/bin/env python3

if __name__ == '__main__':
    N = int(input())
    participants = list(map(int, input().split()))
    main, sub = map(int, input().split())

    remainings = [ (i - main) for i in participants ]
    sub_requires = [ ((i + sub - 1) // sub) for i in remainings if i > 0 ]
    answer = N + sum(sub_requires)
    print(answer)
