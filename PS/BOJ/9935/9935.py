#!/usr/bin/env python3

if __name__ == '__main__':
    origin = input()
    pattern = input()

    pattern_len = len(pattern)
    answer = []
    for c in origin:
        answer.append(c)
        if len(answer) >= pattern_len and answer[-1] == pattern[-1]:
            if ''.join(answer[-pattern_len:]) == pattern:
                del answer[-pattern_len:]
    if len(answer) == 0:
        print('FRULA')
    else:
        print(''.join(answer))
