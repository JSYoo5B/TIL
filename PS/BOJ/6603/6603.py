#!/usr/bin/env python3

def select_numbers(numbers, remaining, selected = []):
    loop_cnt = len(numbers) - remaining + 1
    for i in range(loop_cnt):
        selected.append(numbers[i])
        if remaining == 1:
            yield selected
        else:
            yield from select_numbers(numbers[i+1:], remaining - 1, selected)
        selected.pop()
    return

if __name__ == '__main__':
    while True:
        numbers = list(map(int, input().split()))
        if len(numbers) == 1 and numbers[0] == 0:
            break
        numbers = numbers[1:]
        candidates = select_numbers(numbers, 6)
        for c in candidates:
            print(*c)
        print()
