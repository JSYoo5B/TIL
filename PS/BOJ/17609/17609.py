#!/usr/bin/env python3

def check_palindrome(given):
    middle = len(given) // 2 + 1
    front, back = -1, len(given)
    diff = 0
    while front <= back:
        front += 1
        back -= 1
        if given[front] == given[back]:
            continue
        else:
            forward = given[:back] + given[back+1:]
            backward = forward[::-1]
            if forward == backward:
                diff = 1
                break
            forward = given[:front] + given[front+1:]
            backward = forward[::-1]
            if forward == backward:
                diff = 1
                break
            diff = 2
            break

    return diff


if __name__ == '__main__':
    test_cnt = int(input())
    for _ in range(test_cnt):
        given = input()
        answer = check_palindrome(given)
        print(answer)
