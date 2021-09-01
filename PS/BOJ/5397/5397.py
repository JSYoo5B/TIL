#!/usr/bin/env python3

if __name__ == '__main__':
    test_cnt = int(input())
    for _ in range(test_cnt):
        keylog = input()
        left, right = [], []
        for c in keylog:
            if c == '<' and len(left) > 0:
                right.append(left.pop())
            elif c == '>' and len(right) > 0:
                left.append(right.pop())
            elif c == '-' and len(left) > 0:
                left.pop()
            elif c != '<' and c != '>' and c != '-':
                left.append(c)
        right.reverse()
        answer = ''.join(left + right)
        print(answer)
