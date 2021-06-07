import sys; sys.stdin = open('input_data/16928.txt')
from collections import deque

ladder_num, snake_num = map(int, sys.stdin.readline().split())
ladders = dict()
for _ in range(ladder_num+snake_num):
    start, end = map(int, sys.stdin.readline().split())
    ladders[start] = end
Ground = [0] + [100000]*101

Q = deque()
Q.append([1, 0])
while Q:
    now, before = Q.popleft()
    if now >= 94:
        print(Ground[before] + 1)
        break
    if Ground[now] > Ground[before] + 1:
        Ground[now] = Ground[before] + 1
        for i in range(1, 7):
            if now + i in ladders.keys():
                Q.append([ladders[now + i], now])
            else:
                Q.append([now + i, now])

