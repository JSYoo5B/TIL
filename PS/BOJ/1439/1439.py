#!/usr/bin/env python3

if __name__ == '__main__':
    origin = input()
    set_cnt = len([ s for s in origin.split('1') if len(s) > 0])
    reset_cnt = len([ s for s in origin.split('0') if len(s) > 0])
    answer = min(set_cnt, reset_cnt)
    print(answer)
