#!/usr/bin/env python3

if __name__ == '__main__':
    train_speed, fly_speed, train_dist = map(int, input().split())
    time_elapsed = train_dist // (train_speed * 2)
    fly_dist = fly_speed * time_elapsed
    print(fly_dist)
