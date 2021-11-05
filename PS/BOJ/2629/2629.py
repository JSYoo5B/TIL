#!/usr/bin/env python3

if __name__ == '__main__':
    weight_cnt = int(input())
    weights = list(map(int, input().split()))
    marbles_cnt = int(input())
    marbles = list(map(int, input().split()))

    avails = [ False for _ in range(sum(weights) + 1) ]
    avails[0] = True
    for w in weights:
        for idx, elem in enumerate(avails[:]):
            if elem == True and avails[idx + w] == False:
                avails[idx+w] = True

    for w in weights:
        for idx, elem in enumerate(avails[:]):
            if elem == True and idx - w >= 0 and avails[idx-w] == False:
                avails[idx-w] = True

    for m in marbles:
        if m >= len(avails) or avails[m] == False:
            print("N ", end="")
        else:
            print("Y ", end="")
