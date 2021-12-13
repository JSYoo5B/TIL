#!/usr/bin/env python3

if __name__ == '__main__':
    nums_len, min_sum = map(int, input().split())
    numbers = list(map(int, input().split()))
    sums, total = [0], 0
    for n in numbers:
        total += n
        sums.append(total)

    answer = nums_len + 1
    l, r = 0, 1
    while l < nums_len:
        local_sum = sums[r] - sums[l]
        if local_sum >= min_sum:
            answer = min(answer, r-l)
            l += 1
        else:
            if r < nums_len:
                r += 1
            else:
                l += 1

        if answer == 1:
            break
    if answer == nums_len + 1:
        print(0)
    else:
        print(answer)
