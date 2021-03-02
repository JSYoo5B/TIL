#!/usr/bin/env python3

def bin_search(numbers, num):
    left, right = 0, len(numbers)-1
    found = False
    while found == False:
        mid = (left + right) // 2
        if num < numbers[mid]:
            right = mid - 1
        elif num == numbers[mid]:
            found = True
        else:
            left = mid + 1

        if left > right:
            break
    return found

if __name__ == '__main__':
    num_count = int(input())
    numbers = list(map(int, input().split()))
    numbers.sort()
    find_count = int(input())
    finds = list(map(int, input().split()))
    for n in finds:
        if bin_search(numbers, n):
            print(1)
        else:
            print(0)
