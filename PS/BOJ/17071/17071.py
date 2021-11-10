#!/usr/bin/env python3

from collections import deque

POS_LIMIT = 500000

def get_updated_pos(origin, time_elapsed):
    upd_pos = origin
    upd_pos += time_elapsed * (time_elapsed + 1) // 2
    return upd_pos


def predict_runner_poses(runner_pos):
    predicts = [ ]
    pred_pos = runner_pos
    time_elapsed = 0
    while True:
        pred_pos += time_elapsed
        if pred_pos > POS_LIMIT:
            break
        predicts.append(pred_pos)
        time_elapsed += 1
    return predicts


def get_chase_time(chaser_pos, runner_pos):
    if chaser_pos == runner_pos:
        return 0
    
    predicts = predict_runner_poses(runner_pos)
    visit_info = [ [-1, -1, -1] for _ in range(POS_LIMIT + 1) ]
    for i in range(len(predicts)):
        visit_info[predicts[i]][0] = i

    max_time = len(predicts) - 1
    min_time_elapsed = POS_LIMIT
    que = deque([ [chaser_pos, 0] ])
    visit_info[chaser_pos][2] = 0
    while len(que) > 0:
        [cur_pos, time_elapsed] = que.popleft()
        if time_elapsed > max_time:
            if min_time_elapsed == POS_LIMIT:
                min_time_elapsed = -1
            break
        req_time = visit_info[cur_pos][0]
        if time_elapsed <= req_time \
                and (req_time - time_elapsed) % 2 == 0:
            min_time_elapsed = min(min_time_elapsed, req_time)
            if predicts[time_elapsed] >= cur_pos:
                break
        for new_pos in [cur_pos - 1, cur_pos + 1, cur_pos * 2]:
            if 0 > new_pos or new_pos > POS_LIMIT:
                continue
            if visit_info[new_pos][time_elapsed % 2 + 1] == -1:
                visit_info[new_pos][time_elapsed % 2 + 1] = time_elapsed + 1
                que.append([new_pos, time_elapsed + 1])
    return min_time_elapsed


if __name__ == '__main__':
    older, younger = map(int, input().split())
    answer = get_chase_time(older, younger)
    print(answer)
