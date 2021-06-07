import sys; sys.stdin = open('input_data/16948.txt')
from collections import deque

from pprint import pprint

dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]

size = int(input())
Ground = [[10000]*(size) for _ in range(size)]
start_x, start_y, end_x, end_y = map(int, input().split())
Ground[start_x][start_y] = 0
Q = deque()
Q.append([start_x, start_y])
keep_going = True
if abs(start_x - end_x)%2:
    print(-1)
    keep_going = False
else:
    gap_x = abs(start_x - end_x)//2
    if gap_x%2:
        if not abs(start_y - end_y) % 2:
            print(-1)
            keep_going = False
    else:
        if abs(start_y - end_y) % 2:
            print(-1)
            keep_going = False

if keep_going:
    while Q:
        now_x, now_y= Q.popleft()
        for i in range(6):
            tx = now_x + dx[i]
            ty = now_y + dy[i]
            if 0 <= tx < size and 0 <= ty < size and Ground[tx][ty] > Ground[now_x][now_y] + 1:
                Ground[tx][ty] = Ground[now_x][now_y] + 1
                Q.append([tx, ty])
    print(Ground[end_x][end_y])