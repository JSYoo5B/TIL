#!/usr/bin/env python3

from collections import deque

def printer_queue(priors, target_doc):
    docs = [ [priors[i], i] for i in range(len(priors)) ]
    doc_queue = deque(docs)
    cnt = 0
    while True:
        pending = doc_queue.popleft()
        if len(doc_queue) == 0:
            cnt += 1
            break
        if pending[0] >= max(doc_queue)[0]:
            cnt += 1
            if pending[1] == target_doc:
                break
        else:
            doc_queue.append(pending)
    return cnt

if __name__ == '__main__':
    cnt_tests = int(input())
    for _ in range(cnt_tests):
        cnt_docs, target_doc = map(int, input().split())
        priors = list(map(int, input().split()))
        answer = printer_queue(priors, target_doc)
        print(answer)
