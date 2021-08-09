#!/usr/bin/env python3

if __name__ == '__main__':
    hour, minute = map(int, input().split())

    minute -= 45
    if minute < 0:
        minute += 60
        hour -= 1
        hour += 24
        hour %= 24

    print(hour, minute)
