#!/usr/bin/env python3

from collections import deque

if __name__ == '__main__':
    alpha_cnt = int(input())
    text = input()
    
    zip_text = []
    for t in text:
        if len(zip_text) == 0 or zip_text[-1][0] != t:
            zip_text.append([t, 1])
        else:
            zip_text[-1][1] += 1

    answer = 0
    avail_text, sel_chars = [], set()
    for char, length in zip_text:
        if len(sel_chars) == alpha_cnt and char not in sel_chars:
            remain_chars = set()
            del_char, del_idx = 0, 0
            for idx in range(len(avail_text)-1, -1, -1):
                if avail_text[idx][0] in remain_chars:
                    continue
                if len(remain_chars) < alpha_cnt - 1:
                    remain_chars.add(avail_text[idx][0])
                else:
                    del_char = avail_text[idx][0]
                    del_idx = idx + 1
                    break
            avail_text = avail_text[del_idx:]
            sel_chars.discard(del_char)
        avail_text.append([char, length])
        sel_chars.add(char)
        local_max = sum([t[1] for t in avail_text])
        answer = max(answer, local_max)

    print(answer)
