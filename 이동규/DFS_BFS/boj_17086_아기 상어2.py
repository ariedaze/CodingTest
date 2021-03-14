import sys
sys.stdin = open('input/boj_17086_아기 상어2.txt', 'r')

from collections import deque

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

ROW, COL = list(map(int, input().split()))
MAP = [list(map(int, input().split())) for _ in range(ROW)]
visit = [[-1 for _ in range(COL)] for _ in range(ROW)]
queue = deque()

for r in range(ROW):
    for c in range(COL):
        if MAP[r][c] == 1:
            visit[r][c] = 0
            queue.append([r, c, 0])

while queue:
    r, c, d = queue.popleft()
    for i in range(8):
        dr, dc = r + dx[i], c + dy[i]
        if 0 <= dr < ROW and 0 <= dc < COL and visit[dr][dc] == -1:
            queue.append([dr, dc, d+1])
            visit[dr][dc] = d+1

print(max(map(max, visit)))
