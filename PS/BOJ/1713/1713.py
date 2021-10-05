#!/usr/bin/env python3

UNREGISTERED = 10000

if __name__ == '__main__':
    max_candidate_cnt = int(input())
    recommend_cnt = int(input())
    recommends = list(map(int, input().split()))

    candidate_stats = [ 0 for _ in range(100) ]
    registered_times = [ UNREGISTERED for _ in range(100) ]
    cur_time = -1
    for r in recommends:
        r -= 1 # offset student id from 1~100 to 0~99
        cur_time += 1

        # When the recommended student were in candidate, just increase
        if candidate_stats[r] > 0:
            candidate_stats[r] += 1
            continue
        
        cur_candidate_cnt = 100 - candidate_stats.count(0)
        if cur_candidate_cnt >= max_candidate_cnt:
            min_voted = min([s for s in candidate_stats if s > 0])
            deprecated_id = candidate_stats.index(min_voted)

            if candidate_stats.count(min_voted) > 1:
                min_ids = [ i for i, val in enumerate(candidate_stats) \
                        if val == min_voted ]
                # Find oldest candidate
                oldest_time = min([registered_times[i] for i in min_ids])
                deprecated_id = registered_times.index(oldest_time)
            
            # Remove candidate info
            registered_times[deprecated_id] = UNREGISTERED
            candidate_stats[deprecated_id] = 0
            
        # Register new candidate
        registered_times[r] = cur_time
        candidate_stats[r] = 1

    candidates = [ i + 1 for i in range(100) if candidate_stats[i] > 0 ]
    print(*candidates)

