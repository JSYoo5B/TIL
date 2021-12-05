#!/usr/bin/env python3

if __name__ == '__main__':
    nums_cnt = int(input())
    numbers = list(map(int, input().split()))

    left, right = 0, nums_cnt-1
    v1, v2 = numbers[0], numbers[-1]
    min_sum = abs(numbers[-1] + numbers[0])
    while left < right:
        val = numbers[left] + numbers[right]
        if min_sum > abs(val):
            v1, v2 = numbers[left], numbers[right]
            min_sum = abs(val)

        if val > 0:
            right -= 1
        elif val < 0:
            left += 1
        else:
            break
        
    print(v1, v2)
